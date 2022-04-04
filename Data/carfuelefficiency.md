#### Spyder : F5로 전체 실행, F9로 부분실행
#### 단순회귀분석 : 두 변수 간의 관계를 직선으로 설명
``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/82108/Desktop/정지훈/Dacon/5674-833_4th/part7/auto-mpg.csv',header=None)
df.head

df.columns= ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
print(df.head)
print('\n')

pd.set_option('display.max_columns', 10)
print(df.head)

print(df.info())
print(df.describe())

print(df['horsepower'])
print(df['horsepower'].unique()) ### 고유값 확인하기
print(df['horsepower'].isnull)
print(df['horsepower'])
print(df['horsepower'].isnull())
print(df['horsepower'].isnull().sum())
print(df['horsepower'].unique())
df['horsepower'].replace('?',np.nan, inplace=True) ### ?를 숫자로 계산할 수 있게 null 값으로 바꾸기
df.dropna(subset=['horsepower'],axis=0,inplace=True) ### subset의 누락 데이터 행 삭제
df['horsepower']=df['horsepower'].astype('float') ### 데이터를 숫자형으로 바꾸기
ndf = df[['mpg','cylinders','horsepower','weight']]
print(ndf.head())
ndf.plot(kind='scatter',x='weight',y='mpg',c='coral',s=10,figsize=(10,5)) ###matplot으로 산점도 그리기, s는 점 크기
plt.show()
%matplotlib inline
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1) ##(행,열,index)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='weight',y='mpg',data=ndf, ax = ax1)
sns.regplot(x='weight',y='mpg',data=ndf,ax=ax2,fit_reg=False) ### 회귀선 x
plt.show()
sns.jointplot(x='weight',y='mpg',data=ndf) 
sns.jointplot(x='weight',y='mpg',kind='reg',data=ndf)
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()
ndf
x=ndf[['weight']]
x
y=ndf['mpg']
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=10)
print(len(x_train))
print(len(x_test))
#sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression
#단순회귀분석 모형 객체 생성
lr = LinearRegression()
lr.fit(x_train,y_train)
r_square = lr.score(x_test,y_test)
lr.fit(x_train)
lr.fit(x_train,y_train)
lr.score(x_test,y_test) #linear regression을 사용할 때 독립변수는 반드시 2차원이어야 한다!!(일차식에서 역행렬을 구하기 위한 조건)
#회귀식의 기울기
print(lr.coef_) 
# 회귀식의 y절편
print(lr.intercept_)

# 모형에 전체 x데이터를 넣어 예측한 값과 실제 y값을 비교
y_hat = lr.predict(x)
y_hat
plt.figure(figsize=(10,5))
ax1=sns.kdeplot(y,label='y')
ax2=sns.kdeplot(y_hat,label='y_hat',ax=ax1)
plt.legend()
plt.show()
```
#### 다항회귀분석 : 2차 이상의 다항함수를 이용하여 두 변수 간의 선형관계 설명
``` python
#기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#데이터 준비
#CSV 파일을 데이터프레임으로 전환
df = pd.read_csv('C:/Users/82108/Desktop/정지훈/Dacon/5674-833_4th/part7/auto-mpg.csv',header=None) #header = None :첫번째 행을 열 이름으로 설정하지 않는다

#열 이름 지정
df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
df

#horsepower 열의 자료형 변경
df['horsepower']
df['horsepower'].values
df['horsepower'].replace('?',np.nan, inplace=True) #?를 처리하기 쉽게 na데이터로 바꾸기
df.dropna(subset=['horsepower'],axis=0,inplace=True) #누락 데이터 행 삭제
df['horsepower']=df['horsepower'].astype('float') #해당 열을 스트링에서 실수형 숫자로 바꿈

#분석에 사용할 열 선택
ndf = df[['mpg','cylinders','horsepower','weight']]

#ndf 데이터를 train data와 test data로 구분(7:3)
x=ndf[['weight']]
y=ndf['mpg']

#train data와 test data로 구분
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=10)

print(x_train.shape)
print(x_test.shape)

#비선형회귀분석 모형 - sklearn 사용
# sklearn에서 필요한 모듈 가져오기
from sklearn.linear_model import LinearRegression #선형회귀분석
from sklearn.preprocessing import PolynomailFeatures #다항식 변환

poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)

#train data로 모형 학습
pr=LinearRegression()
pr.fit(x_train_poly,y_train)

#학습을 마친 모형에 test data를 적용해 결정계수 구하기
x_test_poly = poly.fit_transform(x_test)
r_square = pr.score(x_test_poly,y_test)
print(r_square)

#train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat_test = pr.predict(x_test_poly)

fig=plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(x_train,y_train,'o',label='Train Data')
ax.plot(x_test,y_hat_test,'r+',label='Predicted Value')
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()

# 모형에 전체 x데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
x_poly = poly.fit_transform(x)
y_hat = pr.predict(x_poly)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y,label='y')
ax2= sns.kdeplot(y_hat, label='y_hat',ax=ax1)
plt.legend()
plt.show()
```

#### 단순회귀분석 : 독립변수 x와 종속변수 y간의 선형관계
#### 다항회귀분석 : 독립변수 x와 종속변수 y간의 비선형관계
#### 다중회귀분석 : 다수의 독립변수와 종속변수 y간의 선형관계