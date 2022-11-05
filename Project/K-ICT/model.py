# model.py

"""
This file is a sample code of model.py
"""

import torch
import torch.nn as nn

"""
model_configs : all the arguments necessary for your model design.

EX) model_configs = {"num_blocks" : 6, "activation_func" : 'relu', "norm_layer" : 'batch_norm'} 
"""


""" You can change the model name and implement your model. """


""" [IMPORTANT]
get_classifier function will be imported in evaluation file.
You should pass all the model configuration arguments in the get_classifier function 
so that we can successfully load your exact model
saved in the submitted model checktpoint file. 모든 모델 구성 인수를 전달해야 한다?
"""

class CNNclassification(torch.nn.Module):

    def __init__(self, num_classes=20):
        super(CNNclassification, self).__init__()
        self.layer1 = torch.nn.Sequential(
            # 224
            nn.Conv2d(3, 8, kernel_size=3, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))
        # 112
        self.layer2 = torch.nn.Sequential(
            nn.Conv2d(8, 16, kernel_size=3, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.Dropout(),
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer
        # 56

        self.layer3 = torch.nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),  # cnn layer
            nn.ReLU(),  # activation function
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer
        # 28

        self.layer4 = torch.nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),  # cnn layer
            # 28
            nn.ReLU(),  # activation function
            nn.Dropout(),
            nn.MaxPool2d(kernel_size=2, stride=2))  # pooling layer
        # 14

        self.fc_layer = nn.Linear(12544, num_classes, bias=True)  # fully connected layer(output layer)

        # 가중치 초기화
        torch.nn.init.kaiming_uniform_(self.fc_layer.weight)

    def forward(self, x):
        out = self.layer1(x)  # 1층

        out = self.layer2(out)  # 2층

        out = self.layer3(out)  # 3층

        out = self.layer4(out)  # 4층

        out = out.view(out.size(0), -1)

        out = torch.flatten(out, start_dim=1)  # N차원 배열 -> 1차원 배열

        out = self.fc_layer(out)
        return out


def get_classifier(num_classes=20):
    return CNNclassification(num_classes=num_classes)
