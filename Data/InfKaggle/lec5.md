## Kaggle 데이터분석 5강
#### filter 사용해서 규칙성을 갖는 여러 칼럼 가져오기
``` python
question.filter(regex='Q7').split('-')[0] ### question 데이터 셋에서 Q7이 포함된 항목들을 filter해줌. 이후 split으로 해당 항목을 나누기
answer_Q7 = answer.filter(regex='Q7')
answer_Q7_desc = answer_Q7.describe()
answer_Q7_desc.loc[['top','count']].T.set_index('top').plot.bar()
### answer_Q7의 describe 결과에서 top과 count 행을 뽑은 다음 top파트를 index로 사용하여 그래프 그리기
answer_Q7_count = answer_Q7_count.sort_values('count',ascending = False)
```