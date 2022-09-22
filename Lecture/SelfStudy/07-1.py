#keras에서 패션mnist 데이터셋 불러오기
import numpy as np
from tensorflow import keras
(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()
#데이터셋 파악
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,10,figsize=(10,10))
for i in range(10):
    axs[i].imshow(train_input[i], cmap='gray_r')
    axs[i].axis('off')
plt.show()
#타겟 데이터 파악
print([train_target[i] for i in range(10)])
print(np.unique(train_target, return_counts = True))

#로지스틱 회귀로 패션 아이템 분류하기(그전에 배운거)
#데이터 스케일링 : 확률적 경사하강법을 사용할 때에는 기울기에 민감할 수 밖에 없기에 스케일링 필요
train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1,28*28)
print(train_scaled.shape)

#로지스틱 회귀 실행과 성능까지 보자
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log',max_iter=5, random_state = 42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs = -1)
print(np.mean(scores['test_score']))

# 성능이 떨어지고 아무리 iteration 수를 늘려도 성능이 좋아지지 않음
# 이미지 분류문제는 인공 신경망의 성능이 좋음
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size = 0.2, random_state = 42)
print(train_scaled.shape, train_target.shape)
print(val_scaled.shape, val_target.shape)

# 완전 연결층 구현
dense = keras.layers.Dense(10, activation='softmax',input_shape=(784,))
model = keras.Sequential(dense)

#인공 신경망으로 패션 아이템 분류하기
# 케라스 모델은 훈련 이전에 설정이 필요함
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs = 5)
model.evaluate(val_scaled, val_target)