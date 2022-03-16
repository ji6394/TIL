## Dacon Level 3
#### 데이터 시각화
``` python
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('data/csv')
tc = train.copy() #데이터 시각화를 진행할 때는 copy()메서드로 복사본을 만들고 수행

sns.distplot(tc['value'],kde=False,bins=10) ### kde : 선형그래프, bins : 막대그래프 갯수
plt.axis([0,10,0,2500]) ### matplot그래프의 x축 최소, 최대값, y축 최소, 최대값
plt.title('valueOfWine') ###그래프의 제목
plt.show() ###그래프 출력
```

#### plot() 메서드를 활용하여 선형 그래프 그리기
``` python
import matplotlib
import matplotlib.pyplot as plt

x_values=[0,1,2,3,4]
y_values=[0,1,4,9,16]

plt.plot(x_values,y_values)
plt.show()
```
#### matplotlib로 히스토그램 그리기
``` python
import matplotlib.pyplot as plt
a = [1,2,2,3,3,3,4,4,4,5,6,6,6,6,7,8,9]
plt.hist(a)
plt.show() ###plt.show는 그다지 필요 없는듯
```