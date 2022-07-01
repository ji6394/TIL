# 전국 평균 분양가격
import pandas as pd
df_last = pd.read_csv('주택도시보증공사_전국 평균 분양가격(2019년 12월).csv', encoding='cp949')
df_last.shape
df_last.head()
df_last.tail()

df_first = pd.read_csv('전국 평균 분양가격(2013년 9월부터 2015년 8월까지).csv', encoding='cp949')
df_first.shape
df_first.head()
df_first.tail()