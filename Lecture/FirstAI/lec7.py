#groupby에서 filter 사용하면 유용
import dateutil #string을 date 타입으로 변환
df_phone['date']=df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)
#groupby에서 agg 사용하면 한번에 여러 연산 가능
df_phone.groupby(['month','item']).agg({'duration':sum,'network_type':'count','date':'first'})
grouped = df_phone.groupby('month').agg({'duration':[min,max,np.mean]}) #하나의 칼럼에 대해서도 여러 연산 가능
 
 #pivot table
 df_phone.pivot_table(['duration'], index=[df_phone.month, df_phone.item], columns=df_phone.network, aggfunc='sum', fill_value=0)
 
 #crosstable
 pd.crosstab(index=df_movie.critic, columns = df_movie.title, values = df_movie.rating, aggfunc='first').fillna(0)

 #데이터 시각화
 #matplotlib
 import matplotlib.pyplot as plt
 x = range(100)
 y = [value**2 for value in x]
 plt.plot(x,y)
 plt.show()

import numpy as np
 x_1 = range(100)
 y_1 = [np.cos(value) for value in x_1]

 x_2 = range(100)
 y_2 = [np.sin(value) for value in x_2]

 plt.plot(x_1,y_1)
 plt.plot(x_2,y_2)
 plt.show()

 #color과 linestyle, title, legend 설정 가능
#scatter chart
n=50
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.random.rand(n)
area = np.pi * (15*np.random.rand(n))**2
plt.scatter(x,y,s=area, c=colors, alpha=0.5)
plt.show()

#bar chart
