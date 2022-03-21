#### Spyder : F5로 전체 실행, F9로 부분실행
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
```