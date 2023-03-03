#소수 구하기
#서로 다른 3개의 숫자를 더하여 소수가 되는 경우의 개수 구하기
#itertools : 조합을 튜플로 반환해줌
import itertools
arr = [1,2,3,4]
pm = itertools.combinations(arr,3)
a = list(pm)
for i in a:
    print(sum(i))
# 소수판별 알고리즘 : 에라토스테네스의 체
import math
n = 1000
array = [True for i in range(n+1)] #2부터 1000까지의 수 내에 소수 찾기

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1): #2부터 n의 제곱근까지의 모든 수 확인
    if array[i] == True:#i가 소수인경우
        j = 2
        while i*j <= n:
            array[i*j]= False
            j +=1
#모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end = ' ')
#내가 푼 코드
import itertools
import math
def solution(nums):
    pn = []
    n = 1000
    array = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j <= n:
                array[i*j]=False
                j+=1
    for k in range(2,n+1):
        if array[k]:
            pn.append(k)
    answers=[]
    ra = []
    cb = itertools.combinations(nums,3)
    for i in list(cb):
        answers.append(sum(i))
    for j in answers:
        if j in pn:
            ra.append(j)
    return len(ra)
# but 테스트에서 몇번의 오류
#리스트는 중복 가능?
a=[1]
a.append(1)
print(a)
# ㅇㅇ. 그럼 뭐가 문제?
# 이 경우 나오는 숫자마다 소수 판별하는 것이 더 나은듯?
import math
import itertools
def is_prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    prime_number = []
    for i in itertools.combinations(nums, 3):
        prime_number.append(sum(i))
    for i in prime_number:
        if is_prime_number(i):
            answer += 1
        else:
            continue
    return answer
