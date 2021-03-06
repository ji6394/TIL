#사이킷런 버전확인
import sklearn
print(sklearn.__version__)

#붓꽃 예측을 위한 사이킷런 필요 모듈 로딩
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#데이터 세트 로딩
import pandas as pd
iris= load_iris()
iris_data= iris.data
iris_label = iris.target

iris_df = pd.DataFrame(data = iris_data, columns = iris.feature_names)
iris_df['label'] = iris.target
iris_df.head()

#학습 데이터와 테스트 데이터 세트로 분리
x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11)

#학습 데이터 세트로 학습 수행
dt_clf = DecisionTreeClassifier(random_state=11)

#학습 수행
dt_clf.fit(x_train, y_train)

#테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(x_test)
pred

#예측 정확도 평가
from sklearn.metrics import accuracy_score
print('예측 정확도 : {0:.4f}'. format(accuracy_score(y_test, pred)))

#지도학습은 fit과 predict가 중심인 estimator로 구성됨
#Estimator은 다시 Classifier(분류)와 Regressor(회귀)로 구성
#내장 예제 데이터 셋은 feature_names, data, target_names, target으로 구성됨

#Model Selection - 학습 데이터 셋과 테스트 데이터 셋으로 구분
# train_test_split함수
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=121)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
dt_clf = DecisionTreeClassifier()
train_data = iris.data
train_label = iris.target

x_train, x_test, y_train, y_test = train_test_split(train_data, train_label, test_size=0.3, random_state=121)
dt_clf.fit(x_train, y_train)

pred = dt_clf.predict(x_test)
print('예측정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))

#ndarray뿐만 아니라 판다스 dataframe, series에도 적용 가능
iris_df = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
iris_df['target']=iris_data.target

ftr_df=iris_df.iloc[:,:-1]
tgt_df=iris_df.iloc[:,-1]
x_train, x_test, y_train, y_test = train_test_split(ftr_df, tgt_df, test_size=.3, random_state=121)
dt_clf = DecisionTreeClassifier()
dt_clf.fit(x_train, y_train)
pred = dt_clf.predict(x_test)
print('예측정확도 : {0:.4f}'.format(accuracy_score(y_test,pred)))

#교차검증 : 학습 데이터 셋과 테스트 데이터 셋을 구분한 후 학습 데이터 셋을 다시 나누어 테스트 데이터를 이용하기 전 일차적으로 검증하는 방식
#k-fold 교차검증 : 데이터 셋을 5개로 구분하고 하나씩 번갈아가며 검증평가 후 5개의 검증 결과를 평균치를 냄
# 일반 K 폴드와 Stratified K 폴드로 구분됨. Stratified K 폴드의 경우 불균형한 분포도를 가진 레이블 데이터 집합을 학습데이터와 검증 데이터의 레이블 분포도가 유사하도록 겁증 데이터 추출하는 방식.

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np

iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)

kfold = KFold(n_splits=5)
cv_accuracy=[]

n_iter=0
for train_index, test_index in kfold.split(features):
    x_train, x_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]

    dt_clf.fit(x_train, y_train)
    pred = dt_clf.predict(x_test)
    n_iter += 1

    accuracy = np.round(accuracy_score(y_test, pred),4)
    train_size = x_train.shape[0]
    test_size = x_test.shape[0]

    print('\n#{0} 교차 검증 정확도 :{1}, 학습 데이터 크기 : {2}, 검증 데이터 크기: {3}'.format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스:{1}'.format(n_iter, test_index))

    cv_accuracy.append(accuracy)

print(np.mean(cv_accuracy))

#하지만 이런 방식은 데이터를 나누는데에 있어서 불균형을 야기할 수 잇음
#Stratified K-Fold
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=3)
n_iter=0
dt_clf = DecisionTreeClassifier(random_state=156)
cv_accuracy=[]

for train_index, test_index in skf.split(features, label):
    x_train, x_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]

    dt_clf.fit(x_train, y_train)
    pred = dt_clf.predict(x_test)

    n_iter +=1
    accuracy = np.round(accuracy_score(y_test, pred),4)
    cv_accuracy.append(accuracy)
print(np.mean(cv_accuracy))

#cross_val_score() : stratified 교차검증을 편리하게. 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
import numpy as np

iris_data = load_iris()
dt_clf = DecisionTreeClassifier(random_state=156)

data = iris_data.data
label = iris_data.target

scores = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=3)

#GridSearchCV : 최적 하이퍼 파라미터 도출
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=121)
dtree = DecisionTreeClassifier()
parameters = {'max_depth':[1,2,3], 'min_samples_split':[2,3]}

import pandas as pd

grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3, refit=True, return_test_score=True)

grid_dtree.fit(x_train, y_train)

scores_df = pd.DataFrame(grid_dtree.cv_results_)
scores_df[['params','mean_test_score','rank_test_score','split0_test_score','split1_test_score','split2_test_score']]

grid_dtree.cv_results_
grid_dtree.best_params_
grid_dtree.best_score_

pred = grid_dtree.predict(x_test)
accuracy_score(y_test, pred)


# 데이터 전처리(Preprocessing)
# 데이터 인코딩 - 레이블 인코딩, 원핫인코딩
# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder

items =['TV','냉장고','전자렌지','컴퓨터','선풍기','선풍기','믹서','믹서']
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
print('인코딩 변환값:',labels)
print('인코딩 클래스 :',encoder.classes_)
print('디코딩 원본 값:',encoder.inverse_transform([4, 5, 2, 0, 1, 1, 3, 3]))

#원 핫 인코딩
from sklearn.preprocessing import OneHotEncoder
import numpy as np

items =['TV','냉장고','전자렌지','컴퓨터','선풍기','선풍기','믹서','믹서']
items = np.array(items).reshape(-1,1)
oh_encoder = OneHotEncoder()
oh_encoder.fit(items)
oh_labels = oh_encoder.transform(items)

print('원핫인코딩 데이터')
print(oh_labels.toarray())

print('원핫 인코딩 데이터 차원')
print(oh_labels.shape)

#pd.get_dummies : 원핫 인코딩 실현
import pandas as pd
df = pd.DataFrame({'item':['Tv','냉장고','전자렌지','컴퓨터','선풍기','선풍기','믹서','믹서']})
pd.get_dummies(df)

# 피처 스케일링
# 표준화 : 평균 0, 표준편차 1인 정규분포로 변환
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)
iris_df_scaled = pd.DataFrame(data = iris_scaled, columns = iris.feature_names)

# 정규화 : 0과 1사이의 값으로 변환
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)
iris_scaled_df = pd.DataFrame(data = iris_scaled, columns = iris_df.feature_names)

#정규화할 시 학습 데이터와 테스트 데이터 세트 구분하기(테스트 데이터 세트를 fit하지 않도록 주의)

train_array = np.arange(0,11).reshape(-1,1)
test_array = np.arange(0,6).reshape(-1,1)

scaler = MinMaxScaler()
scaler.fit(train_array)
train_scaled = scaler.transform(train_array)
test_scaled = scaler.transform(test_array)