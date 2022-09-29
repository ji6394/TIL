#합성곱 신경망의 가중치 시각화
from tensorflow import keras
#학습한 모델 불러오기
model = keras.models.load_model('best-cnn-model.h5')
model.layers

conv = model.layers[0]
print(conv.weights[0].shape, conv.weights[1].shape) #첫번째 합성곱 층의 가중치와 절편의 사이즈 출력

conv_weights = conv.weights[0].numpy()
print(conv_weights.mean(), conv_weights.std())

#가중치의 분포 확인
import matplotlib.pyplot as plt
plt.hist(conv_weights.reshape(-1,1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()

#커널 출력
fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i,j].imshow(conv_weights[:,:,0,i*16+j], vmin=-0.5, vmax = 0.5)
        axs[i,j].axis('off')
plt.show()

conv_acti = keras.Model(model.input, model.layers[0].output)
(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()
plt.imshow(train_input[0], cmap='gray_r')
plt.show()

inputs = train_input[0:1].reshape(-1,28,28,1) / 255.0
feature_maps = conv_acti.predict(inputs)

fig, axs = plt.subplots(4,8,figsize=(15,8))
for i in range(4):
    for j in range(8):
        axs[i,j].imshow(feature_maps[0,:,:,i*8+j])
        axs[i,j].axis('off')
plt.show()
