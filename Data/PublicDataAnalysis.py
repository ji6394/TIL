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
