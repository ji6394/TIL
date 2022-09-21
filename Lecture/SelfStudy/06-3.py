#데이터 다운로드
#!wget https://bit.ly/fruits_300_data -O fruits_300.npy
import numpy as np

fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

#100*100개의 차원을 50개의 주성분으로 축소시켜보자
from sklearn.decomposition import PCA
pca = PCA(n_components=50)
print(pca.components_.shape)

#draw_fruits 함수 구현
import matplotlib.pyplot as plt
def draw_fruits(arr, ratio=1):
    n = len(arr)
    rows = int(np.ceil(n/10))
    cols = n if rows<2 else 10
    fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10+j<n:
                axs[i,j].imshow(arr[i*10+j], cmap='gray_r')
            axs[i,j].axis('off')
    plt.show()

#데이터 셋의 50가지 주성분 시각화하기
draw_fruits(pca.components_.reshape(-1,100,100))

#원본 데이터 셋의 차원을 50으로 줄이기
fruits_pca = pca.transform(fruits_2d)

#차원이 줄어든 데이터 셋을 원본으로 변환하기
fruits_inverse = pca.inverse_transform(fruits_pca)

#원본으로 돌아온 데이터로 출력해보기
fruits_reconstruct = fruits_inverse.reshape(-1,100,100)
for start in [0,100,200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print('\n')

#설명된 분산 : 주성분이 원본 데이터의 분산을 얼마나 잘 설명하는 지를 나타내는 수치
pca.explained_variance_ratio_

#지도학습에 PCA알고리즘 적용해보기
#로지스틱 회귀분석
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
#타겟 데이터 생성
target = np.array([0]*100,[1]*100,[2]*100)
#교차 검증 통해 모델 성능 파악
from sklearn.model_selection import cross_validate
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

#주성분분석을 이용한 모델이 성능도, 시간도 우월

#주성분 분석 모델링 시 주성분 개수가 아닌 설명된 분산의 비율에 맞추어 모델링도 가능
pca = PCA(n_components=0.5)
pca.fit(fruits_2d)

print(pca.components_) #50%에 달하는 설명력에 대응되는 주성분 개수는 2개

#주성분으로 변환시키기
fruits_pca = pca.transform(fruits_2d)

#교차검증으로 모델 성능 파악
scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

#로지스틱 회귀가 아닌 K-Means 알고리즘으로 모델 성능 파악
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, random_state = 42)
km.fit(fruits_2d)
print(np.unique(km.labels_, return_counts=True))

for label in range(3):
    draw_fruits(fruits[km.labels_==label])
    print('\n')

#2차원으로 시각화해보기
for label in range(3):
    data = fruits_pca[km.labels==label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(['apple','banana','pineapple'])
plt.show()