#Pandas
import pandas as pd
df_data.values
from pandas import Series, DataFrame
import pandas as pd
list_data = [1,2,3,4,5]
example_obj = Series(data = list_data)
example_obj

DataFrame(raw_data, columns=['age','city']) #특정 칼럼만 선택하여 로드하기
DataFrame(raw_data, columns=['first_name','last_name','age','city','debt'] #새로운 칼럼 추가하기

#indexing
df.loc[1]
df['age'].iloc[1:]

df.T #전치행렬
df.values #값 출력
df.to)csv() #csv로 변환

del df['debt'] #칼럼 삭제
df.drop(1) #행 삭제
df.drop(['debt'], axis=1) #칼럼 삭제

df['account'].head(3)
df[['account','street','state']].head(3)

df[:3] #정수형으로 인덱싱하면 Row에 적용. 문자형으로 인덱싱하면 column에 적용

#Series Operation
s1 = Series(range(1,6), index=list('abcde'))
s2 = Series(range(5,11), index=list['bcedef'])
s1.add(s2) #인덱스가 같은 것끼리 연산 수행
s1+s2 #위와 동일

df1= DataFrame(np.arange(9).reshape(3,3), columns = list('abc'))
df2 = DataFrame(np.arange(16).reshape(4,4), columns=list('abcd'))
df1+df2
df1.add(df2, fill_value=0)

#map 활용
import numpy as np
s1=Series(np.arange(10))
s1
z={1:'A',2:'B',3:'C'}
s1.map(z)

df.sex.unique()
df['sex_code']=df.sex.map({'male':0, 'female':1})
df.sex.replace(['male','female'],[0,1],inplace=True)

#apply for dataframe
#map과 달리 series 전체(column)에 해당 함수 적용
df_info = df[['earn','height','age']]
f = lambda x: x.max()-x.min()
df.info.apply(f)

def f(x):
    return Series([x.min(), x.max()], index=['min','max'])
df_info.apply(f)

#describe
df.describe()
df.race.unique()
np.array(dict(enumerate(df['race'].unique())))