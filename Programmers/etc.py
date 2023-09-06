# 내적
from math import prod
def solution(a, b):
    answer = 0
    zip_list = zip(a,b)
    for i in zip_list:
        answer += prod(i)
    return answer

#음양 더하기
def solution(absolutes, signs):
    answer = 0
    absolutes = list(absolutes)
    signs = list(signs)
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer+= absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

#로또의 최고최소순위
def solution(lottos, win_nums):
    lottos = list(lottos)
    win_nums = list(win_nums)
    zero_num = lottos.count(0)
    while 0 in lottos:
        lottos.remove(0)
    counting=0
    for i in lottos:
        if i in win_nums:
            counting+=1
    max_count = counting+zero_num
    min_count = counting
    answer=[]
    for i in [max_count, min_count] :
        if i>=2:
            answer.append(7-i)
        else:
            answer.append(6)
    return answer
# 삼총사
from itertools import combinations
def solution(number):
    answer = 0
    ego=[]
    cat = list(combinations(number,3))
    for i in cat:
        ego.append(sum(i))
    for j in ego:
        if j==0:
            answer+=1
    return answer
# 콜라문제 : 런타임 오류
def solution(a, b, n):
    get = 0
    switch= True
    while switch:
        y = n%a
        if y == 0:
            x = n//a
            get+=x
            n = x
            if n <2:
                switch=False
        else:
            x= n//a
            get+=x
            n = x+y
            if n<2:
                switch=False
    return get
# 콜라문제 해결(문제 제대로 안읽음,,ㅋㅋ)
def solution(a, b, n):
    get = 0
    switch= True
    while switch:
        y = n%a
        if y == 0:
            x = b*(n//a)
            get+=x
            n = x
            if n <a:
                switch=False
        else:
            x= b*(n//a)
            get+=x
            n = x+y
            if n<a:
                switch=False
    return get
            
# 옹알이(2)
def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:  # babbling의 단어 하나씩 확인
        for c in can:
            if c * 2 not in bab:  # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
                
        if bab.isspace():  # 공백으로만 이루어져 있으면 answer+1
            answer += 1
            
    return answer
# 햄버거 만들기
def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        if s[-4:]==[1,2,3,1]:
            answer+=1
            del s[-4:]
    return answer
# 푸드 파이트 대회 : 일부 문제 오류
def solution(food):
    s=[]
    answer=[]
    food2=food[1:]
    for i in food2:
        if i % 2 == 1:
            i -= 1
        s.append(int(i/2))
    for j in s:
        for _ in range(j):
            answer.append(s.index(j)+1)
    answer_2 = list(reversed(answer))
    answer_new = answer + [0] + answer_2
    answer_d = list(map(str,answer_new))
    a = ''.join(answer_d)
    return a
# 푸드파이트 정답
def solution(food):
    temp = '' # 왼쪽 선수 음식
    for i in range(1, len(food)):
        temp += str(i) * (food[i]//2)
    return temp + '0' + temp[::-1]
# 과일 장수
def solution(k, m, score):
    score.sort()
    answer=0
    for i in range(len(score)//m):
        l = []
        for j in range(m):
            l.append(score.pop())
        answer += (min(l)*m)
    return answer
# 기사단원의 무기(1) : 런타임 오류
def solution(number, limit, power):
    weak=[]
    for i in range(1,number+1):
        num=0
        for j in range(1,i+1):
            if i%j ==0:
                num+=1
        weak.append(num)
    answer=[]
    for k in weak:
        if k > limit:
            answer.append(power)
        else:
            answer.append(k)
    real_answer=sum(answer)
    return real_answer
# 약수의 개수를 구할 때에 제곱근을 이용하여 2개씩 플러스
def get_cds(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): # ★포인트1. 제곱근만큼만 반복
        if n%i == 0:
            if i == n//i: # 제곱근일 경우 -> 1개만 카운트하기
                cnt += 1
            else:
                cnt += 2 # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
        if cnt > limit:  # ★포인트2. 소수의 개수가 limit를 넘어가면
            return power #            강제로 power만큼을 return 
    return cnt

    
def solution(number, limit, power):
    total = 1
    for i in range(2, number+1):
        len_cds = get_cds(i, limit, power)
        total += len_cds

    return total
# 명예의전당(1)
def solution(k, score):
    top = []
    low = []
    for i in score:
        if len(top)!=k:
            top.append(i)
            low.append(min(top))
        else:
            if i>low[-1]:
                top.remove(low[-1])
                top.append(i)
                low.append(min(top))
            else:
                low.append(min(top))
    return low
# 문자열 나누기
def solution(s):
   answer = 0
   cnt1=0; cnt2=0
   for i in s:
       if cnt1==cnt2:
           answer+=1
           k=i
       if k==i:
           cnt1+=1
       else:
           cnt2+=1
       
   return answer