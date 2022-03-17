## Kaggle을 활용한 데이터분석
``` python
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import seaborn as sns
import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats
set_matplotlib_formats("retina")

plt.style.use("seaborn-whitegrid")

raw = pd.read_csv(r"../input/kaggle-survey-2020/kaggle_survey_2020_responses.csv", low_memory=False)
raw.shape

question = raw.iloc[0]
question

answer = raw.drop([0])
answer
```

``` python
answer['Q1'].value_counts() : 변수 별 빈도수
``` 
```python
answer['Q1'].value_counts(normalize=True) #normalize = True : 변수가 아닌 비율로 나타냄
```
```python
answer['Q1'].value_counts(normalize=True).sort_index() # index에 따라 정렬
```
```python
answer['Q1'].value_counts(normalize=True).sort_index().plot() # 시각화
```
```python
answer['Q1'].value_counts(normalize=True).sort_index().plot.bar() # 세로 막대그래프
```
```python
answer['Q1'].value_counts(normalize=True).sort_index().plot.barh() # 가로 막대그래프
```
``` python
sns.countplot(data=answer.sort_values('Q1'), x='Q1', palette='Blues_r').set_title(question['Q1']) #seaborn 패키지 활용하여 막대그래프 출력. data는 사용할 데이터, x는 x축에 쓸 데이터. set_title()로 해당 그래프의 제목 설정. palette로 그래프에 그라데이션 설정 가능, _r로 역순 설정
```
