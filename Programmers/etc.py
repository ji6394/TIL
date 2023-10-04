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
# 가장 가까운 같은 글자
def solution(s):
    s = list(s)
    comp = []
    result = []
    for i in s:
        if i not in comp:
            result.append(-1)
        else:
            cat = [j for j,v in enumerate(comp) if v == i]
            spot = max(cat)            
            result.append(len(comp)-spot)
        comp.append(i)
    return result
# 크기가작은 부분문자열
def solution(t, p):
    answer=0
    for i in range(len(t)-len(p)+1):
        num = int(t[i:i+len(p)])
        if num <= int(p):
            answer+=1
    return answer
# 개인정보 수집 유효기간
def time_convert(t) :
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    for idx, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer
# 둘만의 암호
def solution(s, skip, index):
    abc = [chr(i) for i in range(97, 123) if not chr(i) in skip] * 3
    answer = ''
    for i in s:
        answer += abc[abc.index(i) + index]
        
    return answer
# 카드 뭉치
def solution(cards1, cards2, goal):
    answer='Yes'
    for i in goal:
        if cards1 and cards1[0]==i:
            cards1.pop(0)
        elif cards2 and cards2[0]==i:
            cards2.pop(0)
        else:
            answer='No'
            break
    return answer
# 덧칠하기
def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer
# 바탕화면 정리(1트)
def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    for i in wallpaper:
        for j in i:
            if j == '#':
                if wallpaper.index(i) < lux:
                    lux = wallpaper.index(i) #lux
                if i.index(j) < luy:
                    luy = i.index(j) #luy
                if wallpaper.index(i)+1 > rdx:
                    rdx = wallpaper.index(i)+1 #rdx
                rev_i = list(reversed(i))
                ind = len(rev_i) - rev_i.index('#')
                if ind > rdy:
                    rdy = ind #rdy
    return [lux,luy,rdx,rdy]
# 바탕화면 정리 풀이
def solution(wallpaper):
    answer = [51, 51, 0, 0]
    lux, luy, rdx, rdy= 0, 1, 2, 3
    
    for i, elements in enumerate(wallpaper):
        for j, element in enumerate(elements):
            if element == '#':
                answer[lux] = min(answer[lux], i)
                answer[luy] = min(answer[luy], j)
                answer[rdx] = max(answer[rdx], i+1)
                answer[rdy] = max(answer[rdy], j+1)
                
    return answer
# 공원 산책
def solution(park, routes):
    # 시작점('S') 찾기
    x, y = 0, 0
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == 'S':  # 시작 지점 'S'
                x, y = row, col
    
    # 이동 방향 정의
    op = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    # 이동
    for i in routes:
        dx, dy = op[i.split()[0]]  # op에서 해당 방향에 맞는 이동 값 dx, dy로 가져오기
        n = int(i.split()[1])  # 이동 횟수
        
        xx, yy = x, y  # n번의 이동 동안 변하는 좌표 저장 xx, yy
        canmove = True  # 이동할 수 있는 route인지 확인
        
        # n번 이동해보기
        for _ in range(n):
            nx = xx + dx  # 이동한 위치
            ny = yy + dy  # 이동한 위치
            
            # 공원 안에 있고, 장애물이 아니면 이동 가능(True)
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                canmove = True
                xx, yy = nx, ny
            else:  # 공원을 벗어낫거나, 장애물이면 이동 불가(False)
                canmove = False
                break
                
        if canmove:  # 이동이 가능하면 위치 반영해주기
            x, y = nx, ny  
        
    return [x, y]