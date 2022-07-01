#CODE-UP 6096 바둑알 십자 뒤집기
a=[]
for i in range(19):
    a.append([])
    for j in range(19):
        a[i].append(0)
for i in range(19):
    a[i]= list(map(int,input().split()))
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    for j in range(19):
        if a[x-1][j]==0:
            a[x-1][j]=1
        else:
            a[x-1][j]=0
        if a[j][y-1]==0:
            a[j][y-1]=1
        else:
            a[j][y-1]=0
for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()


k=[]
for i in range(5):
    k.append([])
    for j in range(5):
        k[i].append(0)
k[0][1]
k

#codeup 6097 설탕과자 뽑기
h,w = map(int, input().split())
a=[]
for i in range(h):
    a.append([])
    for j in range(w):
        a[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int,input().split())
    if d == 0:
        for j in range(l):
            a[x-1][y-1+j]=1
    else:
        for j in range(l):
            a[x-1+j][y-1]=1
for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()

#codeup 6098 성실한 개미
h = []
for i in range(10):
    a = list(map(int, input().split()))
    h.append(a)
x, y = 1, 1
while True:
    if a[x][y]==0:
        a[x][y]=9
    elif a[x][y]==2:
        a[x][y]==9
        break
    if a[x+1][y]==1 & a[x][y+1]==1:
        break
    if a[x+1][y]!=1:
        x=x+1
    elif a[x][y+1]!=1:
        y=y+1
for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()



