## 1강
#### pandas로 dataframe 객체 이용 가능
#### pd.read_csv : 액셀 파일 dataframe으로 읽기
#### csvname.shape : 해당 dataframe의 행과 열 갯수 불러오기
#### .isnull() : 결측치가 있을 시 true 값 리턴, 아닐 경우 false 값 리턴
#### .isnull().sum() : 각 열 별 결측치의 개수 리턴
#### Python 오픈 소스 머신러닝 라이브러리를 통해 ML 모델들 구현 가능
#### scikit - learn 라이브러리 사용
``` python
import sklearn
from sklearn.tree import DecisionTreeClassifier
```
#### 의사결정나무 중 CART 의사결정 나무 : 이진분할 사용. 데이터를 살펴볼 때, 각 행들은 피쳐들을 갖고 있다. 이 중 하나의 피쳐를 정해서 해당 피쳐의 값에 대해 특정한 하나의 값을 정한 후 이를 기준으로 모든 행들을 두 개의 노드(node)로 분류
#### CART 의사 결정 나무는 공평하게 나누는 것이 아닌, 한쪽으로 쏠리게 하는 것이 핵심!
#### from [라이브러리] import [모듈] \n model = 모듈명()
#### fit(x,y) : 예측에 사용되는 x데이터와 예측결과 변수 y데이터 이용하여 모델 훈련
#### 모델 선언 후 모델 훈련
``` python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

train = pd.read_csv('Data/train.csv')
test = pd.read_csv('Data/test.csv')

print(train.isnull().sum())

train.dropna()
test.dropna()

X_train = train.drop(['count'],axis=1)
Y_train = train['count']

model = DecisionTreeRegressor()
model.fit(X_train,Y_train) ### X_train : 자료 , Y_train : 결과 자료, 상위 요소들을 이용하여 fit 메서드로 훈련

pred = model.predict(test) ### 예측하고자 하는 독립변수인 test변수를 이용하여 예측
pred[:5] ### 상위 5개만 추출

submissiondf = pd.read_csv('data/submission.csv') ###submission.csv파일 df 파일로 불러오기

submissiondf['count']=pred
submissiondf.to_csv(index=False) ### csv파일로 내보내기
```
