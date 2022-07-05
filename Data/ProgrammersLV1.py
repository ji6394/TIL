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