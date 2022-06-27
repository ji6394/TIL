## 선형대수학 3강
#### vectors in R^2 : 2차원 벡터
#### 벡터의 곱은 기존 벡터의 연장선상
#### 벡터 u = (u1,u1,...,un)으로도 표현 가능
#### Algebraic properties of R^n
#### u, v, w는 벡터, c , d 는 스칼라
1. u + v = v + u
2. (u + v) + w = u + (v + w)
3. u + 0 = 0 + u = u
4. u + ( -u ) = 0
5. c( u + v ) = cu + cv
6. (c + d)u = cu + cd
7. c(du) = (cd)u
8. 1u = u
#### **linear combination**
- v1, v2, ..., vn에 해당하는 벡터에 c1, c2, c3,...,cn에 해당하는 스칼라를 각각 곱하여 만들 수 있는 모든 조합
- 만약 **a**=(1,-2,-5)이고 **b**=(2,5,6)이며 **c**=(7,4,-3)이라 할 때 c가 a와 b의 linear combination으로 만들어질 수 있는지 확인하기 위해서 (a b c)의 Augmented matrix를 echelon form 으로 만들어서 확인 가능
#### **Span {v1,v2,...,vn}** : All possible linear combination of {v1,v2,...,vn}
#### 벡터 b가 span{v1,...vn}안에 속해있는 지 확인하기 위하여 augmented matrix인 [v1, v2, ..., vn, b]가 solution을 가지는지 확인하면 됨
#### span{u}의 경우 벡터 u의 연장선상
#### span{u,v}의 경우 3차원에서 u의 연장선상과 v의 연장선상을 이은 마름모
#### span{u,v}의 경우에도 b가 속해있는지 augmented matrix의 forward phase를 통해 확인 가능