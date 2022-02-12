## matplotlib
- 대화형 시각화 기능
``` python
%matplotlib notebook
```

- matplotlib 임포트
``` python
import matplotlib.pyplot as plt
```
- 예제1
``` python
import numpy as np
data = np.arange(10)
plt.plot(data)
```
#### matplotlib에서 그래프는 Figure 안에 위치
- figure 만들기
``` python
fig = plt.figure()
```
#### 그래프를 그리기 위해서 반드시 figure 안에 subplot이 존재해야함
``` python
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
```
#### plt.plot()을 사용하면 만약 figure와 subplot이 없을 경우 자동 생성
- subplot 들 간 간격 조절
``` python
subplots_adjust(left=None, bottom = None, right= None, top=None, wspace= None hspace=None)
```
- subplot 간의 간격을 주지않은 그래프 생성
``` python
fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(50), bins=50, color='k', alpha = 0.5)
plt.subplots_adjust(wspace=0, hspace=0)
```
#### 그래프의 색상, 마커, 선 스타일 설정 가능
``` python
plot(randn(30).cumsum(), color='k', linestyle = 'dashed', marked = 'o')
```
- 그래프의 축 눈금, 제목 변경
``` python
ticks = ax.set_xticks([0,250,500,750,100])
labels = ax.set_xticklabels(['one','two','three','four','five'], rotation = 30, fontsize = 'small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
```
- 범례 추가하기
``` python
ax.legend(loc='best')
```
- 주석 추가 예시
``` python
from datetime import datetime

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read('examples/spx.csv', index_col=0, parse_dates=True)
spx=data['SPX']

spx.plot(ax=ax, style = 'k-')

crisis_data = [
    (datetime(2007,10,11),'Peak of bull market'),
    (datetime(2008,3,12),'Bear Stearns Fails'),
    (datetime(2008,9,15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date,spx.asof(date)+75), xytext=(date,spx.asof(date)+225), arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4), horizontalalignment='left',verticalalignment='top')

#2007 - 2010 구간으로 확대
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600,1800])

ax.set_title('Important dates in the 2008-2009 financial crisis')
```
- 그래프를 파일로 저장하기
``` python
plt.savefig('figpath.png', dpi = 400, bbox_inches='tight')
```
#### 수직 막대그래프와 수평 막대 그래프
``` python
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
```
####seaborn 패키지를 활용하여 더욱 간단하게 처리 가능
``` python
import seaborn as sns
sns.barplot(x='tip_pct',y='day', data=tips, orient='h')
```





