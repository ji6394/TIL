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