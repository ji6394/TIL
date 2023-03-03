# 모의고사
# 처음 한 풀이
import numpy as np
def solution(answers):
    length = len(answers)
    a=[]
    b=[]
    c=[]
    for i in length:
        for j in [1,2,3,4,5]:
            if i%5 == j:
                a.append(j)
        if i%2==0:
            b.append(2)
        else:
            j = i//2
            k = j%4
            list = [1,3,4,5]
            b.append(list[k])
        c_list = [3,3,1,1,2,2,4,4,5,5]
        p = i%10
        c.append(c_list[p])
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    answers_np = np.array(answers)
    comp_a = len(a[np.equal(a, answers_np)])
    comp_b = len(b[np.equal(b, answers_np)])
    comp_c = len(c[np.equal(c, answers_np)])
    d = {}
# 마지막에 사람별로 성적을 비교한 뒤 사람의 인덱스를 출력하는 것에 어려움을 겪음
# 다른 방법 search
def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i,v in enumerate(answers):
        if v == pattern1[i%len(pattern1)]:
            score[0] +=1
        if v == pattern2[i%len(pattern2)]:
            score[1] += 1
        if v == pattern2[i%len(pattern3)]:
            score[2] += 1
    for i, v in enumerate(score):
        if v == max(score):
            answer.append(i+1)
    return answer
# 하지만 런타임 오류
# 아래애 코드는 비슷하지만 enumerate를 안써서 runtime에서 이득을 본듯?
def solution(answers):
    answer = []
    person = [0] * 3 # 3명의 수포자가 맞춘 개수를 넣을 리스트
    a1 = [1, 2, 3, 4, 5] # 1번째 수포자의 답을 넣은 리스트
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2번째 수포자의 답을 넣은 리스트
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번째 수포자의 답을 넣은 리스트

    # 맞춘 개수를 확인하는 코드
    for i in range(len(answers)):
        # 1번째 수포자는 5개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a1[i%5]:
            person[0] += 1
        # 2번째 수포자는 8개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a2[i%8]:
            person[1] += 1
        # 3번째 수포자는 10개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a3[i%10]:
            person[2] += 1

    winner = max(person) # 가장 많이 맞춘 사람의 개수를 넣는 변수 
    # 가장 많이 맞춘 사람을 넣는 코드 (공동 1등이 나올 수 있으므로)
    for i in range(len(person)):
        if person[i] == winner:
            answer.append(i+1)
    return answer