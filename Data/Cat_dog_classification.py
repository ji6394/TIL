#!wget --no-check-certificate \
#  https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
#  -O /content/cats_and_dogs_filtered.zip

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, models, transforms
import numpy as np
import matplotlib.pyplot as plt
import torch.optim as optim
from torch.optim import lr_scheduler
import copy
import time

base_dir = '/content/cats_and_dogs_filtered'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

train_cats = os.listdir(train_cats_dir)
train_cats.sort()
train_dogs = os.listdir(train_dogs_dir)
train_dogs.sort()

print(train_cats[:10])
print(train_dogs[:10])

data_transforms = {
    'train':transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
    ]),
    'validation': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
    ]),
}

image_datasets = {x:datasets.ImageFolder(os.path.join(base_dir, x), data_transforms[x])
                  for x in ['train','validation',]}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size = 4, shuffle=True, num_workers=2) for x in ['train','validation']}
dataset_sizes = {x:len(image_datasets[x]) for x in ['train','validation']}
class_names = image_datasets['train'].classes

#dataloader 살펴보기
for i, (img, label) in enumerate(dataloaders['train']):
  print(img.shape)
  print(label)


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
device

def imshow(inp, title=None):
  inp = inp.numpy().transpose((1,2,0))
  #왜 transpose했지?
  mean = np.array([0.485, 0.456, 0.406])
  std = np.array([0.229, 0.224, 0.225])
  inp = std*inp + mean
  inp = np.clip(inp, 0, 1)
  plt.imshow(inp)
  if title is not None:
    plt.title(title)
  plt.pause(0.001)
inputs, classes = next(iter(dataloaders['train']))
out = torchvision.utils.make_grid(inputs)
imshow(out, title=[class_names[x] for x in classes])

def train_model(model, optimizer, criterion, scheduler, num_epochs=25):
  #criterion= loss function
  since = time.time()
  best_model_wts = copy.deepcopy(model.state_dict())
  #state_dict()는 모델로 학습 시 각 layer마다 텐서로 매핑되는 매개변수를 python dictionary 타입으로 저장한 객체
  best_acc = 0.0
  for epochs in range(num_epochs):
    print('Epoch {}/{}'.format(epochs, num_epochs-1))
    for phase in ['train','validation']:
      if phase == 'train':
        model.train()
      else:
        model.eval()

      running_loss = 0.0
      running_corrects = 0

      for i, (inputs, labels) in enumerate(dataloaders[phase]):
        optimizer.zero_grad() #pytorch에서는 gradients 값들을 추후 backward를 할 때 계속 더하기 때문에 0으로 만들어야 정확한 gradient를 더할 수 있음
        inputs = inputs.to(device)
        labels = labels.to(device)#gpu로 해당 모델 불러오기

          #순전파
          #학습 시에만 연산 기록을 추적
        with torch.set_grad_enabled(phase == 'train'):
          outputs = model(inputs)
          _, preds = torch.max(outputs, 1)
            #torch.max()함수는 최대값에 해당하는 values와 indices를 리턴
          loss = criterion(outputs, labels)
            #학습 단계의 경우 역전파 + 최적화
          if phase ==' train':
            loss.backward()
            optimizer.step()
          # 통계
        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)

      if phase == 'train':
        scheduler.step()

      epoch_loss = running_loss / dataset_sizes[phase]
      epoch_acc = running_corrects.double() / dataset_sizes[phase]

      print('{} Loss : {:.4f} Acc : {:.4f}'.format(phase, epoch_loss, epoch_acc))

      if phase == 'validation' and epoch_acc > best_acc:
        best_acc = epoch_acc
        best_model_wts = copy.deepcopy(model.state_dict())

    print()

  time_elapsed = time.time() - since
  print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed %60))
  print('Best val Acc : {:4f}'.format(best_acc))

  model.load_state_dict(best_model_wts)
  return model




def visualize_model(model, num_images = 6):
  #model.training은 뭐지?
  was_training = model.training
  model.eval()
  images_so_far = 0
  fig = plt.figure()

  with torch.no_grad():
    for i, (inputs, labels) in enumerate(dataloaders['validation']):
      inputs = inputs.to(device)
      labels = labels.to(device)

      outputs = model(inputs)
      _, preds = torch.max(outputs, 1)

      for j in range(inputs.size()[0]):
        images_so_far += 1
        ax = plt.subplot(num_images//2, 2, images_so_far)
        ax.axis('off')
        ax.set_title('predicted: {}'.format(class_names[preds[j]]))
        imshow(inputs.cpu().data[j])

        if images_so_far == num_images:
          model.train(mode = was_training)
          return
    model.train(mode=was_training)


model = torchvision.models.vgg16(pretrained=True)
for param in model.parameters():
  param.requires_grad = True

model.classifier._modules['6'] = nn.Linear(4096,2)
parameters = model.classifier._modules['6'].parameters()
model = model.to(device)

#Loss
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(parameters, lr = 0.001)

exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

model = train_model(model, optimizer, criterion, exp_lr_scheduler, num_epochs=20)

visualize_model(model)

plt.ioff()
plt.show()