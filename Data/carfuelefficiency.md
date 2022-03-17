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
```