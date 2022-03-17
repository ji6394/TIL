## Kaggle 데이터분석 4강
#### 사용자 정의 함수로 데이터 시각화
``` python

q1_cols = answer['Q1'].value_counts().sort_index().index.tolist() ## Q1의 답변의 인덱스를 리스트에 넣기
def show_countplot_by_qn(qn,fsize=(10,6),order=None): ##fsize는 plt의 사이즈의 기본값 설정
    if order == None:
        order = answer[qn].value_counts().index
    plt.figure(figsize=fsize)
    sns.countplot(data=answer, y=qn,order = order).set_title(question[qn]) ##order은 값 정렬
show_countplot_by_qn('Q1',fsize=(10,12),q1_cols)
```