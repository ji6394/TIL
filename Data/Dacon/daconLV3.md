## Dacon Level 3
#### 데이터 시각화
``` python
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('data/csv')
tc = train.copy() #데이터 시각화를 진행할 때는 copy()메서드로 복사본을 만들고 수행

sns.distplot(tc['value'],kde=False,bins=10) ### kde : 선형그래프, bins : 막대그래프 갯수
plt.axis([0,10,0,2500]) ### matplot그래프의 x축 최소, 최대값, y축 최소, 최대값
plt.title('valueOfWine') ###그래프의 제목
plt.show() ###그래프 출력
```

#### plot() 메서드를 활용하여 선형 그래프 그리기
``` python
import matplotlib
import matplotlib.pyplot as plt

x_values=[0,1,2,3,4]
y_values=[0,1,4,9,16]

plt.plot(x_values,y_values)
plt.show()
```
#### matplotlib로 히스토그램 그리기
``` python
import matplotlib.pyplot as plt
a = [1,2,2,3,3,3,4,4,4,5,6,6,6,6,7,8,9]
plt.hist(a)
plt.show() ###plt.show는 그다지 필요 없는듯
```

#### boxplot으로 이상치 판별하기
``` python
import pandas as pd
import seaborn as sns

train = pd.read_csv('data/train.csv')

sns.boxplot(data=train['fixed acidity'])
```

#### 이상치 제거하기
``` python
quantile_25 = np.quantile(train['fixed acidity'],0.25)
quantile_75 = np.quantile(train['fixed acidity'],0.75)
IQR = quantile_75-quantile_25
minimum = quantile_25-1.5*IQR
maximum = quantile_75+1.5*IQR
train2 = train[(minimum<=train['fixed acidity'])&(train['fixed acidity']<=maximum)]
```
#### 수치형 데이터 정규화
#### 트리 기반 모델(의사결정나무, 랜덤포레스트)는 대소 비교를 통해 구분하기에 숫자의 단위에 민감하지 않지만 평활함수모델(Lasso, Logistic Regression)은 숫자의 크기와 단위에 민감
#### 수치형 데이터 정규화를 통해 어떤 모델이든 적합하게 사용 가능
#### MinMaxScaling
``` python
train.describe() #데이터의 분포 파악
sns.distplot(train['fixed acidity'])
scaler=MinMaxScaler()
scaler.fit(train[['fixed acidity']]) #대괄호가 두개인 이유는 fit에는 데이터 셋이 들어가야하기 때문, 대괄호 하나는 Series
train['Scaled fixed acidity'] = scaler.transform(train[['fixed acidity']]) #train의 fixed acidity를 새로운 칼럼에 저장
sns.dsitplot(train['Scaled fixed acidity'])
```
#### MinMaxScaler()는 이상치에 민감하기에 이상치를 제거하는 것도 고려
#### One-Hot Encoding : 문자로 된 데이터 전처리, 해당하는 것만 1, 나머지는 0으로 바꿈
``` python
encoder= OneHotEncoder()
encoder.fit(train[['type']])
onehot = encoder.transform(train[['type']])
onehot=onehot.toarray() #onehot변수를 array로 변환
onehot=pd.DataFrame(onehot) ##onehot array를 dataframe으로 변환
onehot.columns=encoder.get_feature_names() #column이름 바꾸기
onehot = pd.concat([train,onehot],axis=1)
train = train.drop(columns=['type'])
```

#### RandomForest 모형으로 분류하기
``` python
from sklearn.ensemble import RandomForestClassifier

random_classifier = RandomForestClassifier()

X = train.drop(['quality'],axis=1)
Y = train['quality']

random_classifier.fit(X,Y)
```
#### KFold로 교차검증하기
``` python
from sklearn.model_selection import KFold

Kf = KFold(n_shuffle = 5, shuffle = True, random_state = 0) ###n_shuffle은 [훈련,검증]의 개수, shuffle은 Fold를 나누기 전 무작위로 섞는지 여부, random_state 는 난수값
model = RandomForestClassifier(random_state = 0)
valid_scores = []
test_predictions = []


for train_idx, test_idx in kf.split(train):
    X_tr = X.iloc[train_idx]
    Y_tr = Y.iloc[train_idx]

    X_val = X.iloc[test_idx]
    Y_val = Y.iloc[test_idx]
    model.fit(X_tr,Y_tr)
    valid_prediction  = model.predict(X_val)
    score = accuracy_score(y_val, valid_prediction)
    valid_scores.append(score)

for train_idx, test_idx in kf.split(train):
    X_tr = X.iloc[train_idx]
    Y_tr = Y.iloc[train_idx]

    X_val = X.iloc[test_idx]
    Y_val = Y.iloc[test_idx]
    model.fit(X_tr,Y_tr)

    test_prediction = model.predict(test.drop(['index'],axis=1))
    test_predictions.append(test_prediction)
test_predictions = pd.DataFrame(test_predictions)
test_prediction = test_predictions.mode()
test_prediction = test_prediction.values[0]

sample_submission = pd.read_csv('data/sample_submission.csv')
sample_submission['quality'] = test_prediction
sample_submission.to_csv('data/submission_KFOLD.csv', index= False)
```