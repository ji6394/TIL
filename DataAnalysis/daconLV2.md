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