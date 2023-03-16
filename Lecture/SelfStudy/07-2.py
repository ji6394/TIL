#데이터셋 로드
import keras
(train_input, train_target), (test_input, test_target)=\
    keras.datasets.fashion_mnist.load_data()
#데이터 전처리
from sklearn.model_selection import train_test_split
train_scaled = train_input /255.0
train_scaled = train_scaled.reshape(-1,28*28)
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size = 0.2, random_state = 42)

#비선형적인 은닉층을 추가해야만 밀집층의 효과가 있음
dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))
dense2 = keras.layers.Dense(10, activation='softmax')

#심층 신경망 만들기
#은닉층과 출력층의 순서대로 나열해야 함
model = keras.Sequential([dense1, dense2])
model.summary()

#층을 추가하는 다른 방법
#1 : Sequential 클래스 내 생성자로 Dense 클래스의 객체 만들기
model = keras.Sequential([
    keras.layers.Dense(100, activation='sigmoid', input_shape=(784,), name='hidden'),
    keras.layers.Dense(10, activation='softmax', name='output')
], name='패션 MNIST 모델')
model.summary()
#2 : add()메서드 활용
model = keras.Sequential()
model.add(keras.layers.Dense(100, activation='sigmoid', input_shape = (784,)))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()

#모델 훈련시키기
model.compile(loss='sparse_categorical_crossentropy',metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

#ReLU함수
# 초창기 인공 신경망의 은닉층에는 sigmoid가 사용됨. 하지만 오른쪽과 왼쪽 끝으로 갈수록 그래프가 누워있는 개형이기에 올바른 출력을 신속히 만들지 못함
# ReLU = max(0, z)
#Flatten은 케라스에서 제공하는 클래스로 배치 차원을 제외하고 나머지 입력차원을 모두 일렬로 펼치는 역할
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape = (28,28)))
model.add(keras.layers.Dense(100, activation = 'relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()

#옵티마이저 : 케라스에서 제공하는 다양한 종류의 경사하강법 알고리즘
# 기본 설정 알고리즘은 RMSprop
# SGD(이름은 SGD이지만 미니배치를 사용함)
# 기본 경사하강법 옵티마이저는 모두 SGD클래스에서 제공하며 momentum(이전 그레디언트를 가속도로 사용. 기본값은 0)과 nesterov(기본값 False. 모멘텀 최적화를 2번 반복하여 구현. 대부분 기본 확률적 경사 하강법보다 좋은 성능)
# 적응적 학습률 : 모델이 최적점에 가까이 갈수록 학습률을 낮추고 안정적으로 최적점에 수렴할 가능성을 높이는 모델
# 적응적 학습률을 사용하는 모델에는 RMSprop, Adagrad가 있으며 모멘텀 최적화와 RMSprop의 장점을 접목한 모델이 Adam
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape = (28,28)))
model.add(keras.layers.Dense(100, activation = 'relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs = 5)
model.evaluate(val_scaled, val_target)