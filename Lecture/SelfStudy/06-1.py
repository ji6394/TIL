#colab에서 데이터 불러오기
#!wget https://bit.ly/fruits_300_data -O fruits_300.npy

import numpy as np
import matplotlib.pyplot as plt

fruits = np.load('fruits_300.npy')
print(fruits.shape)

print(fruits[0,0,:])
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

fig, ax = plt.subplots(1,2)
ax[0].imshow(fruits[100], cmap='gray_r')
ax[1].imshow(fruits[200], cmap='gray_r')
plt.show()

#픽셀값 분석
apple = fruits[:100,].reshape(-1,100*100)
pineapple = fruits[100:200].reshape(-1,100*100)
banana = fruits[200:300].reshape(-1,100*100)

#샘플 평균값 비교
plt.hist(np.mean(apple, axis=1), alpha = 0.8)
plt.hist(np.mean(pineapple, axis=1), alpha = 0.8)
plt.hist(np.mean(banana, axis=1), alpha = 0.8)
plt.legend(['apple','pineapple','banana'])
plt.show()
#픽셀 평균값 비교
fig, axs = plt.subplots(1,3, figsize=(20,5))
axs[0].bar(range(10000), np.mean(apple, axis=0))
axs[0].bar(range(10000), np.mean(pineapple, axis=0))
axs[0].bar(range(10000), np.mean(banana, axis=0))
plt.show()

apple_mean = np.mean(apple, axis=0).reshape(100,100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100,100)
banana_mean = np.mean(banana, axis=0).reshape(100,100)

fig, ax = plt.subplots(1,3, figsize=(20,5))
ax[0].imshow(apple_mean, cmap = 'gray_r')
ax[1].imshow(pineapple_mean, cmap = 'gray_r')
ax[2].imshow(banana_mean, cmap='gray_r')
plt.show()

#사과의 픽셀 평균값과 가까운 사진 고르기
abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
print(abs_mean.shape)

apple_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10,10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i,j].imshow(fruits[apple_index[i*10+j]], cmap='gray_r')
        axs[i,j].axis('off')
plt.show()