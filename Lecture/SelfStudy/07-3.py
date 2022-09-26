#신경망 모델 훈련
#fit() 메서드로 모델은 훈련하면 훈련 과정이 출력됨(epochs, 손실, 정확도 등)
from html.entities import html5
from tensorflow import keras
from sklearn.model_selection import train_test_split
(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()
train_scaled = train_input / 255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(train_input, train_target, test_size = 0.2, random_state=42)

#모델 함수
def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28,28)))
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer:
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model

model = model_fn()
model.summary()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=5, verbose=0)
print(history.history.keys())

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

plt.plot(history.history['accuracy'])
plt.show()

#검증 손실 계산
model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data=(val_scaled, val_target))

print(history.history.keys())
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

#옵티마이저 변경
model = model_fn()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs = 20, verbose=0, validation_data = (val_scaled, val_target))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

#드롭아웃 : 훈련 과정에서 층에 있는 일부 뉴런을 랜덤하게 꺼서 과대적합을 방지함
model = model_fn(keras.layers.Dropout(0.3))
model.summary()

#모델 저장과 복원
model = model_fn()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs = 20, verbose=0, validation_data = (val_scaled, val_target))
#모델 파라미터만 저장
model.save_weights('model-weights.h5')
#모델 구조 + 모델 파라미터 저장
model.save('model-whole.h5')
#파일 확인
!ls -al *.h5

#저장된 파일 불러오기
model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('model-weights.h5')
#검증 정확도 확인
import numpy as np
val_labels = np.argmax(model.predict(val_scaled), axis=-1)
print(np.mean(val_labels == val_target))

#전체 모델 불러오기
model = keras.models.load_model('model-whole.h5')
model.evaluate(val_scaled, val_target)

#콜백
#ModelCheckpoint : 에포크마다 모델을 저장하며 가장 낮은 검증 점수를 만드는 모델을 저장할 수 있음
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data = (val_scaled, val_target), callbacks=[checkpoint_cb])
model.keras.load_model('best-model.h5')
model.evaluate(val_scaled, val_target)

#EarlyStopping : 검증 점수가 향상되지 않더라도 참을 에포크 횟수인 patience, 가장 낮은 검증 손실을 낸 모델 파라미터로 되돌리는 restore_best_weights를 사용 가능
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data = (val_scaled, val_target), callbacks=[checkpoint_cb, early_stopping_cb])
print(early_stopping_cb.stopped_epoch)
model.evaluate(val_scaled, val_target)