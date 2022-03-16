## 데이터분석 Chapter 10: 데이터 집계와 그룹 연산
#### groupby
``` python
df['data1'].groupby(df['key1']).mean()
df['data1'].groupby([df['key1'],df['key2']])
```
#### groupby 이터레이션(이름,묶음)
``` python
for name, group in df.groupby('key1'):
    print(name)
    print(group)
```
#### groupby는 딕셔너리, Series, 함수로 그룹핑 가능
#### multiindex로 열을 구성하였을 경우 level 예약어를 사용