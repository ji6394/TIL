## Dacon Level4
#### seaborn pairplot : 데이터에 들어 있는 각 열들의 모든 상관관계 출력, grid형태로 히스토그램과 분포도 그림
``` python
data = train.loc[:,'fixed acidity':'chlorides']
sns.pairplot(data)
```
#### distplot은 데이터의 히스토그램 그려주는 함수, 히스토그램은 변수가 하나이다. 변수를 여러 개의 bin으로 자르고 bin당 관측수를 막대그래프로 표현한다.
``` python
data = train['fixed acidity']
sns.distplot(data,bins=100)
```
#### 히트맵(heatmap) : 두 개의 범주형 변수에 대한 반응 변수의 크기를 색깔로 표현한 것
``` python
data = train.corr()
sns.heatmap(data)
```
#### 다중공선성 : 상관관계가 높은 독립분셔둘의 동시에 모델에 포함될 때 발생, 두 변수가 완벽하게 다중공선성에 있다면 같은 변수를 두번 넣은 것으로 모델의 결괏값 추론에 오류 가능
#### 다중공선성 확인하는 방법
1. scatter plot을 통해 확인
2. Heatmap 그래프를 통해 확인
3. VIF(Variance Inflation Factors, 분산팽창요인)을 통한 확인
#### Scatter plot을 통한 다중공선성 확인
``` python
x_data = train['residual sugar']
y_data = train['density']

sns.scatterplot(x=x_data,y=y_data)
```
#### VIF(varainace Inflation Factor,분산팽창요인) : VIF는 변수간의 다중공선성을 진단하는 수치, 범위는 1부터 무한대, 통계학에서는 10이상이면 다중공선성 인정
#### VIFk = 1/1-R^2 (vifk는 k번째 변수의 vif값, R^2은 회귀분석에 사용하는 결정계수)
``` python
vif =[]
train_val=train.values
for i in range(len(train.columns)):
    vif.append(variance_inflation_factor(train_val,))
```