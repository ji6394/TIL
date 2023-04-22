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