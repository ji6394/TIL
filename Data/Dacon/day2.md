## Data analysis p.396~
#### quantile : 해당 백분위 요소 추출
``` python
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
```
#### 컬럼에 여러 가지 함수를 적용하기 위해서는 aggregate 함수 적용
``` python
grouped = tips.groupby(['day','smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
```
``` python
grouped_pct.agg([('foo','mean'),('bar',np.std)])
#(name, function) : function대신 name으로 컬럼 구성
```
``` python
grouped_pct.agg({'tip':np.max, 'size':'sum'})
# 딕셔너리를 통해 칼럼마다 다른 함수 적용
```
#### as_index=False : 그룹키를 색인으로 적용하지 않고 데이터 반환
``` python
tips.groupby(['day','smoker'], as_index=False).mean()
```
#### group_keys=False : 원본 객체의 색인과 그룹 키가 계층적 색인으로 사용되는 것을 막아줌
``` python
tips.groupby('smoker', group_keys=False).apply(top)
```
#### 여러 통계 한번에 사용하기
``` python
def get_stats(group):
    return {'min':group.min(), 'max':group.max(),'count':group.count(),'mean':group.mean()}
grouped = frame.data2.groupby(quartiles)
grouped.apply(get_stats).unstack()
```
#### fillna메서드를 통해 결측치 채울 수 있음

#### 가중평균 구하기
``` python
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])

grouped.apply(get_wavg)
```

#### parse_dates=True : 날짜를 datetime 형태로 변환할 지 여부

#### 피벗 테이블 : 데이터를 하나 이상의 키로 수집해서 어떤 키는 로우에, 어떠 ㄴ키는 컬럼에 나열하여 데이터 정렬
``` python
tips.pivot_table(index=['day','smoker'])
```
``` python
tips.pivot_table(['tips_pct','size'], index = ['time','day'], columns='smoker', margins = True)
#margins=True : 부분합 구하기
```
#### crosstab(교차일람표) : 그룹 빈도를 계산하기 위한 피벗테이블의 종류
``` python
pd.crosstab(data.Nationality, data.Handedness, margins=True)
```

