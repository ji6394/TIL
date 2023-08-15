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
            