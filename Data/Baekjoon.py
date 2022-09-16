# 요세푸스
n, k = map(int, input().split())
lst=[]
for i in range(1, n+1):
    lst.append(i)
answer = []
pt = 0

for i in range(n):
    pt += k-1
    if pt>=len(lst):
        pt = pt%len(lst)
    answer.append(str(lst.pop(pt)))
print('<',', '.join(answer)[:], '>', sep='')
# 쇠막대기
a = list(input())
s=[]
b = 0

for i in range(len(a)):
    if a[i] == '(':
        s.append('(')

    else:
        if a[i-1] == '(':
            s.pop()
            b=b+len(s)

        else:
            s.pop()
            b=b+1
print(b)