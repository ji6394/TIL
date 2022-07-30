#이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
#별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
n, m = map(int, input().split())
for i in range(m):
    for j in range(n):
        print('*', end='')
    print()

#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x+x*i)
    return answer

#행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

#프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
#전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
def solution(phone_number):
    phone_number = phone_number.replace(phone_number[:-4],'*'*len(phone_number[:-4]))
    return phone_number

#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
def solution(x):
    a=str(x)
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    c=list(map(int,b))
    d=sum(c)
    return int(a)%d==0

#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
def solution(arr):
    return sum(arr)/len(arr)

#1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

#1-1. 입력된 수가 짝수라면 2로 나눕니다. 
#1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
#2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
#예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
def solution(num):
    answer = 0
    while True:
        if num ==1:
            break
        if num %2 == 0:
            num = num/2
            answer +=1
        else:
            num = num*3+1
            answer +=1
        if num ==1:
            break;
    if answer>500:
        answer = -1
    return answer

#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
def solution(n, m):
    answer = []
    mini = 1
    maxi = 1
    if n > m:
        for i in range(1,m+1):
            if (n%i==0)and(m%i==0):
                mini=i
        for j in range(n,n*m+1):
            if (j%n==0)and(j%m==0):
                maxi=j
                break
    else:
        for i in range(1,n+1):
            if (n%i==0)and(m%i==0):
                mini=i
        for j in range(m,n*m+1):
            if (j%n==0)and(j%m==0):
                maxi=j
                break
    answer.append(mini)
    answer.append(maxi)
    return answer
#정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
def solution(num):
    if num%2==0:
        answer = 'Even'
    else:
        answer='Odd'
    return answer

#정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
def solution(arr):
    if len(arr)>1:
        a = min(arr)
        arr.remove(a)
        return arr
    else:
        return [-1]

#임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
#n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
def solution(n):
    a = n**(1/2)
    if float.is_integer(a):
        return (a+1)**2
    else:
        return -1
#함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
def solution(n):
    a=str(n)
    b=list(map(int,a))
    b.sort(reverse=True)
    c=0
    for i in range(len(b)):
        c=c+b[i]*10**(len(b)-1-i)
    return c
#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
def solution(n):
    a=list(map(int,str(n)))
    a.reverse()
    return a
#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(n):
    a = list(map(int,str(n)))
    answer = sum(a)
    return answer
#문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]
#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
def solution(n):
    a=[]
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
    return sum(a)
#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    return ''.join(s)
#문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
def solution(s):
    if s[0]=='-':
        s=-int(s[1:])
    else:
        s=int(s)
    return s
#길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
def solution(n):
    a=''
    for i in range(n):
        if i %2==0:
            a+='수'
        else:
            a+='박'
    return a
#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

#소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
#(1은 소수가 아닙니다.)
def solution(n):
    a=[2]
    for i in range(3,n+1):
        b=[]
        for j in range(1,i+1):
            if i%j ==0:
                b.append(j)
        if b == [1,i]:
            a.append(i)            
    return len(a)
# 위와 같은 방식은 시간이 너무 오래걸림
#에라토스테네스의 체 사용!
def solution(n):
    a = [0]*(n+1)
    for i in range(2,len(a)):
        for j in range(2,len(a)):
            idx = i*j
            if idx>n:
                break
            a[idx]=1
    return a[2:].count(0)
#String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
def solution(seoul):
    position = seoul.index('Kim')
    answer = '김서방은 %d에 있다' % position
    return answer
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
def solution(s):
    a = (len(s)==4) or (len(s))==6
    b=True
    try:
        int(s)
    except:
        b=False
    return a and b
#문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
def solution(s):
    s=list(s)
    for i in range(len(s)):
        s[i]=ord(s[i])
    s.sort(reverse=True)
    for i in range(len(s)):
        s[i]=chr(s[i])
    return ''.join(s)
#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

#예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
def solution(s):
    pn = s.count('p')+s.count('P')
    yn = s.count('y')+s.count('Y')
    answer=True
    if pn != yn:
        answer = False
    return answer
#문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
import numpy as np
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])
#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b):
    answer=0
    if b>a:
        for i in range(a,b+1):
            answer +=i
    elif a>b:
        for i in range(b,a+1):
            answer +=i
    else:
        answer = a
    return answer
#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor ==0:
            answer.append(i)
    if answer==[]:
        answer.append(-1)
    answer.sort()
    return answer

#배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

#arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
#arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
#배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if answer[-1]==i:
            continue
        answer.append(i)
    return answer
# 다트게임
import re
def solution(dartResult):
    p = re.compile('[0-9]*[A-Z]\\*?\\#?')
    result = p.findall(dartResult)
    answer=[]
    for i in result:
        if i[-1]=='*':
            a = int(i[:-2])
            if i[-2]=='S':
                a = a
            elif i[-2]=='D':
                a = a**2
            elif i[-2]=='T':
                a = a**3
            a = a*2
            if len(answer)!=0:
                answer[-1]=answer[-1]*2
            answer.append(a)
        elif i[-1]=='#':
            a = int(i[:-2])
            if i[-2]=='S':
                a = a
            elif i[-2]=='D':
                a = a**2
            elif i[-2]=='T':
                a = a**3
            a = -a
            answer.append(a)
        else:
            a = int(i[:-1])
            if i[-1]=='S':
                a = a
            elif i[-1]=='D':
                a = a**2
            elif i[-1]=='T':
                a = a**3
            answer.append(a)
    return sum(answer)
#가운데 글자 가져오기
def solution(s):
    if len(s)%2==0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[(len(s)//2)]
#비밀지도
def solution(n, arr1, arr2):
    sq=[]
    for i in range(n):
        sq.append([])
        for j in range(n):
            sq[i].append(' ')
            c_1 = format(arr1[i],'b').zfill(n)
            if c_1[j]=='1':
                sq[i][j]='#'
            d_1 = format(arr2[i],'b').zfill(n)
            if d_1[j]=='1':
                sq[i][j]='#'
        sq[i]=''.join(sq[i])
    return sq
            
# 부족한 금액 계산하기
def solution(price, money, count):
    need = 0
    for i in range(1,count+1):
        need += price*i
    if need - money >0:
        return need - money
    else:
        return 0
# 나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(1,n):
        if n%i == 1:
            return i
# 최소직사각형
def solution(sizes):
    lst=[]
    for size in sizes:
        lst.append([max(size),min(size)])
    a, b = zip(*lst)
    x=max(a)
    y=max(b)
    return x*y
# 2016년
import datetime
def solution(a, b):
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = days[datetime.date(2016,a,b).weekday()]
    return answer
# 두 개 뽑아서 더하기
def solution(numbers):
    lst = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a=numbers[i]+numbers[j]
            lst.add(a)
    answer=list(lst)
    answer.sort()
    return answer
# 예산
def solution(d, budget):
    lst=[]
    d.sort()
    for i in d:
        if sum(lst)+i>budget:
            break
        lst.append(i)
    return len(lst)
# 3진법 뒤집기
def solution(n):
    b=True
    a=[]
    if n<3:
        a.append(n)
        b=False
    while b:
        n,r = divmod(n,3)
        a.append(r)
        if n<3:
            a.append(n)
            break
    answer = 0
    for k,i in enumerate(a):
        answer += i*(3**(len(a)-(k+1)))
        print(answer)
    return answer
# 약수의 개수와 덧셈
def solution(left, right):
    answer = []
    for i in range(left, right+1):
        check=[]
        for j in range(1,i):
            if i%j == 0:
                check.append(j)
        if len(check)%2==0:
            answer.append(-i)
        else:
            answer.append(i)
    return sum(answer)
# 카펫
def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
# 이중우선순위큐
def solution(operations):
    answer=[]
    for i in range(len(operations)):
        a,b = operations[i].split()
        b=int(b)
        if a == 'I':
            answer.append(b)
            answer.sort()
        elif a =='D':
            if answer==[]:
                continue
            else:
                if b==-1:
                    del answer[0]
                else:
                    answer.pop()
    if answer==[]:
        answer=[0,0]
    return [max(answer), min(answer)]
# 실패율
import numpy as np
def solution(N, stages):
    answer = []
    dic={}
    stages= np.array(stages)
    for i in range(1,N+1):
        try:
            fail = (len(stages[np.where(stages==i)]))/(len(stages[np.where(stages>=i)]))
        except:
            fail = 0
        dic[i]=fail
    sol = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    for a,b in sol:
        answer.append(a)
    return answer
