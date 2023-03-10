## 선형대수학 8강
#### Matrix of Linear Transformation
### 정리 10 : T가 n스페이스에서 m스페이스로의 linear transformation이라 할 때, n차원의 모든 x에 대해서 T(x) = Ax 를 만족하는 유일한 A 행렬이 존재한다.
#### 이 때, A=[T(e1)...T(en)]
#### onto : n차원에서 m차원으로의 transformation인 T가, 적어도 하나의 n차원의 요소의 이미지가 m차원에 있을 때 성립
#### one-to-one : transformation T가 일대일 대응의 관계에 있을 때
### 정리 11 : T(x)=0이 trivial solution만 가질 때, T는 one-to-one이다. 즉, T = Ax인 선형사상일 때, columns of A는 linearly independent하다.이는 선형사상 T가 free variable을 갖지 않아야 함을 말한다.
### 정리 12 : T가 onto일 때, A의 columns는 R^m의 span이다. 즉, Ax=b를 만족시키는 해가 존재하며 이는 A의 각 row는 pivot position을 갖는다.