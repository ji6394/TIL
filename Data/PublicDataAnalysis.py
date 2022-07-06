# 전국 평균 분양가격
#데이터 로드
import pandas as pd
df_last = pd.read_csv('주택도시보증공사_전국 평균 분양가격(2019년 12월).csv', encoding='cp949')
df_last.shape
df_last.head()
df_last.tail()

df_first = pd.read_csv('전국 평균 분양가격(2013년 9월부터 2015년 8월까지).csv', encoding='cp949')
df_first.shape
df_first.head()
df_first.tail()

#결측치 처리
df_last.info()
df_last.isnull().sum()
df_last.isna.sum()
df_last['분양가격(㎡)'].astype(int)
pd.to_numeric(df_last['분양가격(㎡)'])
#shift+tab키를 누르면 옵션 두두둥장
df_last['분양가격']=pd.to_numeric(df_last['분양가격(㎡)'], errors='coerce')
df_last['분양가격'].mean()
df_last['평당분양가격']=df_last['분양가격']*3.3 #평당 가격으로 맞추기

#내용 수정하기
df_last['전용면적']=df_last['규모구분'].str.replace('전용면적','')
df_last['전용면적']=df_last['전용면적'].str.replace('초과','~')
df_last['전용면적']=df_last['전용면적'].str.replace('이하','')
df_last['전용면적']=df_last['전용면적'].str.replace(' ','').str.strip() #공백 없애기

#칼럼 제거
df_last.drop(['규모구분','분양가격(㎡)'],axis=1,inplace=True)

#groupby
dataframe.groupby(['인덱스로 사용할 칼럼'])['결과출력할 칼럼'].mean()

df_last.groupby(['지역명'])['평당분양가격'].mean()
df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack() #뒤의 칼럼을 데이터프레임의 열로 변경
df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack().round().transpose()#행과 열 변경

#pivot table
pd.pivot_table(df_last, index=['지역명'], values=['평당분양가격'], aggfunc='mean')
pd.pivot_table(df_last, index=['전용면적'], columns=['지역명'], values=['평당분양가격'], aggfunc='mean')

#데이터 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
g=df_last.groupby(['지역명'])['평당분양가격'].mean().sort_values(ascending=False)
g.plot.bar(rot=0, figsize=(10,3))
