# 내적
from math import prod
def solution(a, b):
    answer = 0
    zip_list = zip(a,b)
    for i in zip_list:
        answer += prod(i)
    return answer