# Numpy : Numerical Python. 고성능 과학 계산용 패키지. 일반 리스트에 비해 빠르고 반복문 없이 데이터 배열에 대한 처리 지원
import numpy as np
test_array = np.array(['1','4',5,8], float)
print(test_array)
type(test_array[3])
type(test_array[0])
test_array.dtype
test_array.shape
tensor = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]],[[1,2,5,8],[1,2,5,8],[1,2,5,8]],[[1,2,5,8],[1,2,5,8],[1,2,5,8]],[[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
tensor = np.array(tensor, int)
tensor.shape #면,행,렬
tensor.ndim #면의 개수
tensor.size #데이터의 개수
test_matrix=[[1,2,3,4],[1,2,5,8]]
test_matrix = np.array(test_matrix)
test_matrix.shape

np.array(test_matrix).reshape(2,2,2)

np.array(test_matrix).reshape(-1,2) #로우의 개수 상관없이 칼럼에 맞춰서 매트릭스 생성

#flatten : 다차원 행렬을 1차원으로 변형. reshape과 유사
np.array(test_matrix).flatten()

#np.arange
np.arange(30).reshape(5,6)

#np.zeros
np.zeros(shape=(10,), dtype=np.int8)

#np.ones
np.ones(shape=(10,), dtype=np.int8)

#np.identity : 단위행렬
np.identity(n=3, dtype=np.int8)
np.identity(5)

#np.eye : 대각선이 1인 행렬
np.eye(N=3, M=5, dtype=np.int8)
np.eye(N=3, M=5, k=2)

#diag : 대각 행렬의 값 추출
matrix = np.arange(9).reshape(3,3)
np.diag(matrix)

#계산
test_array.sum(dtype=np.float)
test_array.sum(axis=0) #행기준
test_array.sum(axis=1) #열기준

#concatenate
a = np.array([1,2,3])
b = np.array([4,5,6])
np.vstack((a,b))
np.hstack((a,b))

#broadcasting : shape이 다른 배열 간 연산 지원
test_matrix = np.array([[1,2,3],[4,5,6]], float)
scalar=3
test_matrix + scalar

#all & any
a = np.arange(10)
a>5
np.any(a>5)
np.all(a>5)

#np.where
np.where(a>5, 3, 2)
np.where(a>5)

#argmax & argmin
a = np.array([1,2,3,5,9,78,26,3])
a.argmax() #인덱스 값 리턴
a.argmin()
a = np.array([[1,2,4,7],[9,88,6,45],[9,76,3,4]])
np.argmax(a, axis=1)
np.argmin(a,axis=0)

#fancy index
a = np.array([2,4,6,8], float)
b = np.array([0,0,1,3,2,1], int)
a[b]
a.take(b)