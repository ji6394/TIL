``` python
import sklearn
print(sklearn.__version__)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd
iris = load_iris()
iris_data = iris.data
iris_label = iris.target
iris_df = pd.DataFrame(data = iris_data, columns = iris.targete_names)
iris_df['label'] = iris.target

x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state = 11)

dt_clf = DecisionTreeClassifier(random_state=11)

dt_clf.fit(x_train, y_train)

pred = dt_clf.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))
```
#### data는 피처의 데이터 세트
#### target은 레이블 값
#### target_names는 개별 레이블의 이름
#### feature_names는 피처의 이름
#### DESCR은 데이터 세트에 대한 설명과 각 피처의 설명