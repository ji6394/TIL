## 선형대수학 2.5
#### Matrix Factorization : 두개 이상의 matrix들의 곱
#### A= LU
#### 이 때 L행렬은 lower triangular matrix
#### U행렬은 echelon form
#### 이 때 only row replacement만 행해야 한다
#### Ax = B의 해를 구할 때, LUx=B, Ux = y라 할 때, Ly = B로 해를 구할 수 있다.
#### L과 U 행렬을 구하는 방법
- Elementary matrix들의 곱과 A를 곱한 것이 U 행렬
- L 행렬은 elementary matrix의 역행렬들의 곱
#### 만약 interchange가 반드시 필요한 경우 PA = LU로 표현 가능. L행렬의 경우 interchange가 나왔을 때 바로 앞의 row교환
#### 만약 A행렬이 sparse(대부분의 값이 0)일 때, L과 U는 sparse하지만 A의 인버스는 dense하다.