#!wget https://bit.ly/fruits_300_data -O fruits_300.npy
# K-Means 모델을 위해 3차원 배열을 2차원 배열로 변환
import numpy as np
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1,100*100)

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state = 42)
km.fit(fruits_2d)

#군집 결과 리턴
print(km.labels_)
print(np.unique(km.labels_, return_counts = True))

#결과 그림 출력 함수
import matplotlib.pyplot as plt
def draw_fruits(arr, ratio=1):
    n = len(arr)
    rows = int(np.ceil(n/10))
    cols = n if rows<2 else 10
    fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10+j<n:
                if i*10+j<n:
                    axs[i,j].imshow(arr[i*10+j], cmap='gray_r')
                axs[i,j].axis('off')
    plt.show()

#차원이 같기 때문에 fruits_2d 대신에 fruits 사용 가능
draw_fruits(fruits[km.labels_==0])
draw_fruits(fruits[km.labels_==1])
draw_fruits(fruits[km.labels_==2])

#클러스터의 중심 출력
draw_fruits(km.cluster_centers_.reshape(-1,100,100), ratio=3)

#클러스터 중심까지 거리 출력
#2차원 배열이 필요하기에 fruits_2d[100]을 사용하면 안 됨
print(km.trnasform(fruits_2d[100:101]))

#클러스터 중심 예측
print(km.predict(fruits_2d[100:101]))

draw_fruits(fruits[100:101])

# 알고리즘 반복 횟수 출력
print(km.n_iter_)

#최적의 K 찾기 : K-평균 알고리즘의 단점은 클러스터 개수를 사전에 파악하고 있어야함
# 클러스터 개수를 모를 때는 엘보우 방법을 이용
# 엘보우 방법 : K-평균 알고리즘의 클러스터 중심과 클러스터에 속한 샘플 사이의 거리를 이너셔라고 함
# 클러스터 개수의 변화에 따라 이너셔의 감소 기울기 변화를 파악
inertia = []
for k in range(2,7):
    km = KMeans(n_clusters=k, random_state = 42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)
plt.plot(range(2,7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()