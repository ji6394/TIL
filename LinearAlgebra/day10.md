## 선형대수학 10강
#### Invertible Matrix : n*n행렬인 A가 다음 조건을 만족하는 행렬 C를 가질 때 Invertible하다고 한다
- CA = I
- AC = I
#### nonsingular matrix : invertible
#### singular matrix : not invertible
#### 2 * 2 행렬일 때, det A = ad-bc
#### A^-1 = 1/detA[d,-b/-c,a]
#### A가 invertible하고 Ax=b일때, x = A^-1b이다
#### (AB)^-1=B^-1A^-1
#### A가 invertible matrix일 때, A의 transpose의 inverse = A의 inverse의 transpose
#### Elementary matrices : identity matrix에 row operation을 한 번 행한 행렬
#### elementary row operation of matrix A : EA
#### E는 Identity matrix에 같은 row operation을 행하여 만들 수 있음
#### A가 invertible하면 Identity matrix와 row equivalent하다
#### A의 역행렬을 찾는 방법 : A와 크기가 같은 identity matrix를 합쳐 augmented matrix를 만들고 A를 row operation을 행했을 때 identity matrix의 변환결과가 A의 역행렬이다.
