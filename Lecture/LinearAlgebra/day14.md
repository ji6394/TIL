## 선형대수학 16강
#### Subspace of R^n
#### R^n space에 있는 모든 집합 H는 다음 특성을 갖는다
1. 0벡터가 H안에 있다.
2. H안에 있는 u벡터와 v벡터의 경우 u+v벡터도 H안에 있다
3. H안에 있는 u벡터와 scalar c의 경우 cu 벡터도 H안에 있다.
#### v1과 v2가 R^n에 있을 경우 H = span(v1,v2)
#### Subspace
- Column Space(Col A) : A벡터의 칼럼들의 모든 linear combinations, (벡터 b가 Col A안에 있는가?) == (Ax=b 가 consistent한가?)
- Null Space(Nul A) : Ax=0을 만족하는 모든 solutions, (벡터 u가 Nul A안에 있는가?) == (Au=0을 만족하는가?)
#### Basis : subspace H의 linearly independet set
#### Standard Basis for R^n : elementary vector로 이루어진 basis
#### 특정 matrix의 null space의 basis를 구하기 위해서는 homogeneous matrix의 augmented matrix를 만들고 그 solution을 구하였을 때 나오는 벡터의 span에 해당
#### 특정 matrix의 column space의 basis를 구하기 위해서는 row operations를 한 후 pivot columns에 해당하는 원래의 columns의 span이 basis에 해당
