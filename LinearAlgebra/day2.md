## 선형대수학 2강 : Row reduction and Echelon Forms
#### nonzero row and columns : 0이 아닌 행 또는 열
#### A leading entry of row : 각 행에서 0이 아닌 가장 왼쪽의 요소
#### Echelon form(행 사다리꼴) : nonzero 행이 all zero 행보다 위에 위치하고 각 행의 leading entry가 그보다 상위의 leading entry보다 오른쪽에 위치하는 행렬
#### Reduced Echelon form(기약 행 사다리꼴) : Echelon form을 만족하고 각 행의 leading entry가 1이며, leading entry가 각 열에서 유일한 nonzero 요소인 행렬
### 정리 1 : Uniqueness of the Reduced Echelon Form
 : 각 행렬은 자신의 reduced echelon form과 row equivalent하다
#### 행렬을 Echelon form으로 만드는 과정을 forward phase, echelon form을 reduced echelon form으로 만드는 과정을 backward phase라고 한다.
#### 해를 도출할 때 leading entry의 경우 basic variables이지만 nonleading entry의 경우 free variables가 된다.
### 정리 2 : Existence and Uniqueness Theorem
: 각 linear equation에서 consistent(해가 존재)할 경우 [0,0,0,0,0,a]와 같은 행은 존재하지 않는다. 또한, 해가 존재할 경우 free variable이 하나도 존재하지 않으면 unique solution, free variable이 하나 이상 존재할 경우 infinitely many solutions를 가진다.