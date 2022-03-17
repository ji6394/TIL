## LV2 전처리
#### 파이썬 결측치 대체 평균
``` python
df.fillna({'칼럼명' : int(df['칼럼명'].mean)}, inplace = True)
```
#### 생각해보니 다음과 결과가 같다
``` python
df.fillna(df.mean(),inplace=True) ### 마찬가지로 해당 칼럼의 평균을 결측치에 대입해줌
```
#### interpolate : 보간법
#### 데이터에 결측치가 있을 때 바로 직전 값과 직후 값을 이용하여 두 값의 평균을 결측치에 대입하기. 선형보간법이라고 불림
``` python
df.interpolate(inplace=True)
```
#### 랜덤포레스트 : 여러 개의 의사결정나무를 만들어서 이들의 평균으로 예측의 성능을 높이는 방법, 앙상블 기법
``` python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
```
#### 랜덤포레스트의 모듈의 옵션 중 criterion 옵션을 통해 어떤 평가척도를 기준으로 훈련할 것인지를 정할 수 있음
#### MSE(평균제곱오차) : 오차의 제곱의 평균
#### RMSE 는 MSE에 제곱근 취한 것
``` python
model = RandomForestRegressor(criterion='mse')
```
#### fit()으로 모델이 학습되고 나면 feature_importances_ 속성(attribute)로 변수의 중요도를 파악할 수 있다
#### 변수의 중요도 : 예측변수를 결정할 때 각 피쳐가 얼마나 중요한 역할을 하는지에 대한 척도
#### 변수의 중요도가 낮다면 해당 피쳐를 제거하는 것이 성능 높일 수 있음
``` python

model = RandomForestRegressor(criterion='mse') # 모델에 RandomForestRegressor 대입
model.fit(X_train,Y_train) #해당 모델을 이용하여 훈련
model.feature_importances_
# 각 변수의 중요도 측정
```
#### 각 모델 별로 예측하고 결과값 저장하기 : 각 모델 별로 다른 셋 만들고 이를 이용하기
#### 예측할 때 사용되는 test셋은 각 train셋과 같은 피쳐 공유해야함
#### 하이퍼파라미터 튜닝 : 정지규칙 값 설정
#### 의사결정나무에는 정지 규칙이라는 것이 존재
#### 정지 규칙
1. 최대 깊이(max_depth) : 최대로 내려갈 수 있는 depth, 작을수록 트리는 작아짐
2. 최소 노드크기(min_samples_split) : 노드를 분할하기 위한 데이터 수, 해당 노드에 이 값보다 적은 확률변수 수가 있으면 stop,작을수록 크기는 커짐
3. 최소 향상도(min_impurity_decrease) : 노드를 분할하기 위한 최소 향상도, 작을수록 트리 크기가 커짐
4. 비용복잡도(Cost-complexity) : 트리가 커지는 것에 대해 페널티 계수 설정. 불순도와 트리가 커지는 것에 대해 복잡도 계산

#### 위 정지 규칙들을 종합적으로 고려하여 최적의 조건값 설정하는 것이 하이퍼파리미터 튜닝
#### 다양한 방법론이 존재하지만 그 중 Best 성능을 나타내는 GridSearch는 완전 탐색(Exhaustive Search) 사용
#### Best조합을 탐색할 때 까지 시간이 오래걸림

#### GridSearchCv로 하이퍼파리미터 구현하기
``` python
from sklearn.model_selection import GridSearchCV

model = RandomForestRegressor(criterion = 'mse', random_state = 2020) ## 추출값 고정시키기
params = {'n_estimators':[200,300,500],'max_features':[5,6,8],'min_samples_leaf':[1,3,5]}### parameter 설정하기
greedy_CV = gridSearchCV(model,param_grid=params, cv=3,n_jobs=-1) ### cv는 교차검증, n_jobs=-1 : 컴퓨터의 모든 코어 사용
greedy_CV.fit(X_train, Y_train)

pred = greedy_CV.predict(test)
```

