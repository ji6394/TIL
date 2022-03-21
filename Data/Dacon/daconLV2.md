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
#### Bayesian Optimization
#### 하이퍼 파라미터 튜닝 중 GridSearch와 RandomSearch의 경우 최적의 값을 찾아갈 수 없다는 문제
#### Bayesian Optimization은 'Gausian Process'라는 통계학 기반 모델로 여러개의 하이퍼파라미터들에 대해 Aquisition Function을 적용했을 때 가장 큰 값이 나올 확률이 높은 지점을 찾아낸다.
#### Bayesian Optimization을 사용하기 위해서 다음 단계가 필요하다
1. 변경할 하이퍼 파라미터의 범위를 설정한다.
2. Bayesian Optimization 패키지를 통해, 하이퍼 파라미터의 범위 속 값들을 랜덤하게 가져온다.
3. 처음 n번은 랜덤하게 좌표를 꺼내 성능을 확인
4. 이후 m번은 bayesian optimization을 통해 최적의 값을 찾는다.
``` python
!pip install bayesian-optimization ### Jupyter notebook에서는 !을 앞에 붙여 패키지 설치
from bayes_opt import BayesianOptimization
```
#### 하이퍼파라미터 튜닝 방법 3가지 비교
- GridSearch : 탐색할 값들을 미리 지정, 값들의 조합으로 성능의 최고점을 찾는 기법
    - 장점 : 내가 원하는 범위를 정확하게 비교 분석 가능
    - 단점 : 시간이 오래걸림, 성능의 최고점이 아닐 가능성, 최적화 검색(여러개들을 비교분석하여 최고를 찾는 기법), 최적화 탐색(성능이 높은 점으로 점차 이동)이 아니다.
- Random Search : 사전에 탐색할 값들의 범위를 지정, 그 범위 속 가능한 조합을 바탕으로 최고점 찾기
    - 장점 : Gridsearch에 비해 시간이 적게 걸림, 랜덤하게 점을 찍으므로 성능이 더 좋은 점으로 갈 가능성이 높아짐
    - 단점 : 랜덤하게 찍는 것이 오히려 성능 낮출수도, 하이퍼파라미터의 범위가 너무 넓으면 일반화된 결과과 나오지 않음, seed를 고정하지 않으면 결과가 가변적이다, 최적화 검색이지 최적화 탐색이 아니다.
- BayesianOptimization : 하이퍼파라미터의 범위를 지정한 후, Random하게 n번 탐색 후 m번 만큼 최적의 값 찾아냄
    - 장점 : 최적의 값 찾을 수 있음, 상대적으로 시간이 덜 걸림
    - 단점 : Random하게 점을 찍으므로 최적화 하는데 오래걸릴수도, 최적의 값을 찾는게 불가능할 수도, 최적화 이전에 이미 최적값을 보유할 수도 있음
``` python
## x에 학습할 데이터를, y에 목표변수 저장
x = train.drop(columns=['index','quality'])
y = train['quality']
## 랜덤포레스트의 하이퍼 파라미터의 범위를 dictionary 형태로 지정하기
## key는 랜덤포레스트의 hyperparameter 이름, value는 탐색할 범위
rf_parameter_bounds = {'max_depth':(1,3),'n_estimators' : (30,100),}
## 함수 만들기
def rf_bo(max_depth, n_estimators):#함수의 인자는 위에서 만든 함수의 key 값들
    rf_params = {'max_depth':int(round(max_depth)),'n_estimators' : int(round(n_estimators)),}#함수 속 인자를 통해 받아와 새롭게 하이퍼파라미터 딕셔너리 생성
    rf = RandomForestClassifier(**rf_params) #그 딕셔너리를 바탕으로 모델 생성
    x_train, x_valid, y_train, y_valid = train_test_split(x,y,test_size = 0.2,)#train_test_split활용하여 데이터를 train/valid로 나누기
    rf.fit(x_train,y_train) #모델 학습
    score = accuracy_score(y_valid,rf.predict(x_valild)) #모델 성능 확인
    return score #모델의 점수 반환
BO_rf = BayesianOptimization(f=rf_bo, pbounds = rf_parameter_bounds,random_state=0) #pbounds는 하이퍼파라미터의 최소~최대값
BO_rf.maximize(init_points=5,n_iter=5) #Bayesian Optimization을 실행, init_points는 몇 번 탐색할지, n_iter는 최적 값을 몇 번 찾아갈지
max_params = BO_rf.max['params']
max_params['max_depth']=int(max_params['max_depth'])
max_params['n_estimators']=int(max_params['n_estimators'])
print(max_params)

BO_tuend_rf = RandomForestClassifier(**max_params) #결과 저장
```
