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
    # 추억 점수
    def solution(name, yearning, photo):
        score_dict = dict(zip(name,yearning))
        result=[]
        for i in photo:
            score = 0
            for j in i:
                if j in score_dict:
                    score += score_dict[j]
            result.append(score)
        return result
# 달리기 경주(시간 초과)
def solution(players, callings):
    for i in callings:
        a = players.index(i)
        players[a-1], players[a] = players[a], players[a-1]
    return players
# 달리기 경주 : 딕셔너리를 이용해서 시간 줄임
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for who in callings:
        idx = result[who] # 호명된 선수의 현재 등수
        result[who] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players
# 요격 시스템
def solution(targets):
    targets.sort(key = lambda x:x[1])
    cnt, end = 0, 0
    for s,e in targets:
        if s >= end:
            cnt+=1
            end = e
    return cnt
# 두 원 사이의 정수쌍
import math

def solution(r1, r2):
    answer = 0  
    
    for i in range(1, r2+1):
        high_r1 = math.sqrt(r2**2 - i**2)
        high_r2 = 0 if i>r1 else math.sqrt(r1**2 - i**2)
        
        answer += math.floor(high_r1) - math.ceil(high_r2) + 1
          
    return answer*4
# 연속된 부분 수열의 합
def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    sum = sequence[0]

    while True:
        if sum < k:
            r += 1
            if r == len(sequence): break
            sum += sequence[r]
        else:
            if sum == k:
                if r-l < answer[1]-answer[0]:
                    answer = [l, r]
            sum -= sequence[l]
            l += 1
    return answer
# 과제 진행하기(ing...)
def solution(plans):
    for i in plans:
        h,m = map(int,i[1].split(':'))
        start_time = h*60+m
        i.append(start_time)
    plans.sort(key=lambda x:x[3])
    ing=[]
    result=[]
    for i in range(len(plans)):
        if plans[i+1][3]-plans[i][3]<int(plans[2]):
            ing.append(plans[i][0])
        elif plans[i+1][3]-plans[i][3]>=int(plans[2]):
            result.append(plans[i][0])
#과제 진행하기(ver1) : 시도해봤으나 첫번째 or 두번째 값까지만 리턴해줌
def solution(plans):
    for i in plans:
        h,m = map(int,i[1].split(':'))
        start_time = h*60+m
        i.append(start_time)
    plans.sort(key=lambda x:x[3])
    ing={} #과목과 남은 시간을 함께 입력해주어야 할듯
    result=[]
    for i in range(len(plans)-1):
        working_time = plans[i+1][3]-plans[i][3]
        reserve_time = int(plans[i][2])
        to_do = plans[i][0]
        while working_time > reserve_time: # 작업시간이 남는 경우
            result.append(to_do)
            working_time -= reserve_time
            if ing:#ing에 요소가 있을 경우
                to_do, reserve_time = ing.popitem()
            else:#ing에 요소가 없을 경우 break 해주어야 할듯
                break
        if working_time < reserve_time: #작업시간이 모자랄 경우
            ing[plans[i][0]]=reserve_time
        elif working_time == reserve_time:
            result.append(plans[i][0])
    return result
# 과제 진행하기
def solution(plans):
    for i in plans:
        h,m = map(int,i[1].split(':'))
        start_time = h*60+m
        i.append(start_time)
    plans.sort(key=lambda x:x[3])
    ing={} #과목과 남은 시간을 함께 입력해주어야 할듯
    result=[]
    for i in range(len(plans)-1):
        working_time = plans[i+1][3]-plans[i][3]
        reserve_time = int(plans[i][2])
        to_do = plans[i][0]
        while working_time > reserve_time: # 작업시간이 남는 경우
            result.append(to_do)
            working_time -= reserve_time
            reserve_time = 0
            if ing:#ing에 요소가 있을 경우
                to_do, reserve_time = ing.popitem()
            else:#ing에 요소가 없을 경우 break 해주어야 할듯
                break
        if working_time < reserve_time: #작업시간이 모자랄 경우
            reserve_time -= working_time
            ing[to_do]=reserve_time
            working_time = 0
        elif working_time == reserve_time:
            result.append(to_do)
            reserve_time = 0
            working_time = 0
    # plans의 요소들이 끝난 이후
    result.append(plans[-1][0])
    for i in range(len(ing)):
        to_do, _ = ing.popitem()
        result.append(to_do)
    return result
                
# 광물 캐기
def solution(picks, minerals):
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    score=0
    minerals_new=[]
    for i in minerals:
        if i =='diamond':
            minerals_new.append(0)
        elif i == 'iron':
            minerals_new.append(1)
        else:
            minerals_new.append(2)
    for i in range(len(picks)):#012
        time = picks[i]#1
        ind = 0
        for k in range(time):
            count = 0
            while count <5 and ind<len(minerals):
                score += tired[i][minerals_new[ind]]
                count +=1
                ind+=1
    return score
# 광물캐기 (테스트 케이스는 통과, 채점 약 42점)
def solution(picks, minerals):
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    score=0
    minerals_new=[]
    for i in minerals:
        if i =='diamond':
            minerals_new.append(0)
        elif i == 'iron':
            minerals_new.append(1)
        else:
            minerals_new.append(2)
    ind=0
    for j in range(len(picks)):#012
        time = picks[j]#1
        for k in range(time):
            count = 0
            while count <5 and ind<len(minerals_new):
                score += tired[j][minerals_new[ind]]
                count +=1
                ind+=1
    return score
def solution(picks, minerals):#어떻게 해야 최솟값이 되는지 고려 : 
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    score=0
    minerals_new=[]
    for i in minerals:
        if i =='diamond':
            minerals_new.append(0)
        elif i == 'iron':
            minerals_new.append(1)
        else:
            minerals_new.append(2)
    minerals_new.sort() #di-iron-stone순으로 캐면 제일 좋은거아닌가?
    ind=0
    mineral_state=True
    for j in range(len(picks)):#012
        time = picks[j]#1
        for k in range(time):
            count = 0
            while count <5 and mineral_state:
                score += tired[j][minerals_new[ind]]
                count +=1
                ind+=1
                if ind>=len(minerals_new):
                    mineral_state = False
                    
    return minerals_new
# 광물 캐기 정답(무슨말인지 잘 모르겠따..)
mineral_dict = {
    'diamond' : 0,
    'iron' : 1,
    'stone' : 2
}
cost_mat = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]

def init(minerals) :
    minerals = [mineral_dict[mineral] for mineral in minerals]
    
    return minerals

def generate_mineral_list(minerals) :
    result = list()
    tmp = [0]*3
    for i in range(0, len(minerals), 5) :
        for j in range(5) :
            if i + j >= len(minerals) :
                break
            tmp[minerals[i+j]] += 1
        
        result.append(tmp)    
        tmp = [0]*3
        
    return result

def cal_cost(pick, mineral) :
    return sum([ cost_mat[pick][i] * mineral[i] for i in range(3) ])

def dfs(idx, picks, minerals, cost, max_idx) :
    if idx == max_idx :
        return cost
    
    result = float('inf')
    for i in range(3) :
        if picks[i] == 0 :
            continue
        picks[i] -= 1
        next_cost = cost + cal_cost(i, minerals[idx])
        result = min(result, dfs(idx+1, picks, minerals, next_cost, max_idx))
        picks[i] += 1
        
    return result

def solution(picks, minerals):
    minerals = init(minerals)
    minerals = generate_mineral_list(minerals)
    max_idx = min(sum(picks), len(minerals))
    answer = dfs(0, picks, minerals, 0, max_idx)
    return answer
# 리코챗 로봇
def solution(board):
    # 이동변수 글로벌변수로 설정
    shift_list = []
    # 1. R과 G의 위치 인덱스 찾기
    point = [0,0]
    goal = [0,0]
    for i in board:
        for j in i:
            if j == 'R':
                point = [board.index(i), i.index(j)]
            if j == 'G':
                goal = [board.index(i), i.index(j)]
    # 상하좌우 이동 시 각 이동 별로 이동 변수 설정
    # 좌우 이동과 상하 이동 구분해야할듯
    while point != goal:
        #이동변수 할당
        move = 0
        #좌
        while board[point[0],point[1]-1]=='.':
            point[1] -= 1
            if point[1]==0 or board[point[0], point[1]-1]=='D':# 막힐경우
                move +=1
                break
    # 왼쪽or오른쪽으로 이동했을 때 이후 선택지는 상하 두개 뿐!
    # 상하이동 시 이후 선택지는 좌우 두개 뿐!

# 리코챗 로봇 solution
from collections import *
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    answer = 0
    N = len(board) #가로 size
    M = len(board[0]) #세로 size
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]

    #로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(N) :
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
            if q:
                break

    while q:
        x,y,c = q.popleft()

        #목표 지점(G)에 도착한 경우 이동횟수 반환
        if board[x][y] == 'G':
            return c
        
        # 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            n_x = x
            n_y = y

            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0 <= n_x+dx[i]<N and 0<=n_y+dy[i]<M and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]

            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[n_x][n_y] >c+1:
                dist[n_x][n_y] = c+1
                q.append((n_x, n_y, c+1))
    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1

    
# 당구연습 : 원쿠션 전에 맞는 경우는 어카죠???
import math
def solution(m, n, startX, startY, balls):
    answer = []
    # 목표점을 각 사변에 거리만큼 너머에 가상의 목표점 설정. 이후 최소거리가 나왔을 때 해당 최소거리를 answer에 append
    for goalx, goaly in balls:
        #가상의 점 4개 만들기
        fake=[]
        fake.append([goalx, goaly+2*(n-goaly)])
        fake.append([goalx-2*(m-goalx),goaly])
        fake.append([goalx+2*(m-goalx),goaly])
        fake.append([goalx, goaly-2*(n-goaly)])
        dist = []
        for i in fake:
            dist.append((startX-i[0])**2+(startY-i[1])**2)
        answer.append(min(dist))
    return answer
# 당구 연습 : 남의 풀이를 가져와봣다. 여기서 중요한점은 벽 너머로 가상의 점을 찍는게 핵심인듯
def solve(x, y, startX, startY, ballX, ballY):
    dists = []
    # 위쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 크면 안된다.
    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX)**2 + (ballY - 2*y+startY)**2
        dists.append(d2)
    # 아래쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
    if not (ballX == startX and ballY < startY):
        d2 = (ballX - startX)**2 + (ballY + startY)**2
        dists.append(d2)
    # 왼쪽 벽에 맞는 경우
    # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
    if not (ballY == startY and ballX < startX):
        d2 = (ballX + startX)**2 + (ballY - startY)**2
        dists.append(d2)
    # 오른쪽 벽
    # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
    if not (ballY == startY and ballX > startX):
        d2 = (ballX - 2*x+startX)**2 + (ballY - startY)**2
        dists.append(d2)
    
    return min(dists)
    
def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        answer.append(solve(m, n, startX, startY, ballX, ballY))
    return answer
# 혼자서 하는 틱택토 : 예제는 모두 맞았지만 테스트 케이스에서 많이 틀림
def solution(board):
    # O와 X의 개수를 센다 : O의 개수보다 X의 개수가 같거나 적어야 함
    # 한줄빙고가 두개가 나오면 안됨
    # 9개가 모두 찬 경우 무승부
    def solution(board):
    # O와 X의 개수를 센다 : O의 개수보다 X의 개수가 같거나 적어야 함
    o_num = 0
    x_num = 0
    for i in board:
        for j in i:
            if j=='O':
                o_num += 1
            elif j=='X':
                x_num += 1
    if o_num < x_num:
        return 0
    # 한줄빙고가 두개가 나오면 안됨
    # 제일 위에 첫 줄을 보고 세로 혹은 대각선 한줄 빙고를 파악하면 될듯
    bingo_num = 0
    for k in ['O','X']:
        for i in range(3):
            if board[0][i]==k:
                #세로
                if board[1][i]==k:
                    if board[2][i]==k:
                        bingo_num+=1
        #대각
        if board[0][0]==k and board[1][1]==k and board[2][2]==k:
            bingo_num+=1
        if board[0][2]==k and board[1][1]==k and board[2][0]==k:
            bingo_num+=1
        for i in board:
            if i=='OOO' or i=='XXX':
                bingo_num +=1
    if bingo_num >1:
        return 0
    return 1
    # 9개가 모두 찬 경우 무승부
# 혼자서 하는 틱택토 ver2
def solution(board):
    # O와 X의 개수를 센다 : O의 개수보다 X의 개수가 같거나 적어야 함
    o_num = 0
    x_num = 0
    for i in board:
        for j in i:
            if j=='O':
                o_num += 1
            elif j=='X':
                x_num += 1
    if o_num < x_num or o_num - x_num >=2:
        return 0
    # 한줄빙고가 두개가 나오면 안됨
    # 제일 위에 첫 줄을 보고 세로 혹은 대각선 한줄 빙고를 파악하면 될듯
    o_bingo_num = 0
    x_bingo_num = 0
    for k in ['O','X']:
        for i in range(3):
            if board[0][i]==k:
                #세로
                if board[1][i]==k:
                    if board[2][i]==k:
                        if k == 'O':
                            o_bingo_num +=1
                        else:
                            x_bingo_num +=1
        #대각
        if board[0][0]==k and board[1][1]==k and board[2][2]==k:
            if k == 'O':
                o_bingo_num +=1
            else:
                x_bingo_num +=1
        if board[0][2]==k and board[1][1]==k and board[2][0]==k:
            if k == 'O':
                o_bingo_num +=1
            else:
                x_bingo_num +=1
        for i in board:
            if i=='OOO':
                o_bingo_num +=1
            elif i=='XXX':
                x_bingo_num +=1
    if x_bingo_num != 0 and o_bingo_num !=0:
        return 0
    return 1
    # 9개가 모두 찬 경우 무승부
    # 빙고가 두개 이상 나올수도 있구나!! 단 O빙고와 X빙고를 구분해서 두 빙고가 같이 나오는 것은 제외해야할듯
# 혼자서하는 틱택토 final ver
def solution(board):
    # O와 X의 개수를 센다 : O의 개수보다 X의 개수가 같거나 적어야 함
    o_num = 0
    x_num = 0
    for i in board:
        for j in i:
            if j=='O':
                o_num += 1
            elif j=='X':
                x_num += 1
    if o_num < x_num or o_num - x_num >=2:
        return 0
    # 한줄빙고가 두개가 나오면 안됨
    # 제일 위에 첫 줄을 보고 세로 혹은 대각선 한줄 빙고를 파악하면 될듯
    o_bingo_num = 0
    x_bingo_num = 0
    for k in ['O','X']:
        for i in range(3):
            if board[0][i]==k:
                #세로
                if board[1][i]==k:
                    if board[2][i]==k:
                        if k == 'O':
                            o_bingo_num +=1
                        else:
                            x_bingo_num +=1
        #대각
        if board[0][0]==k and board[1][1]==k and board[2][2]==k:
            if k == 'O':
                o_bingo_num +=1
            else:
                x_bingo_num +=1
        if board[0][2]==k and board[1][1]==k and board[2][0]==k:
            if k == 'O':
                o_bingo_num +=1
            else:
                x_bingo_num +=1
        for i in board:
            if i=='OOO':
                o_bingo_num +=1
            elif i=='XXX':
                x_bingo_num +=1
    if x_bingo_num != 0 and o_bingo_num !=0:
        return 0
    if x_bingo_num>0 and x_num!=o_num:
        return 0
    if o_bingo_num>0 and o_num!=x_num+1:
        return 0
    return 1
    # X를 빙고로 이겼을 때와 O를 빙고를 이겼을 때를 구분하여 o의 개수와 x개수를 함께 고려하니 통과함


# 미로탈출 ing...
from collections import *
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    N = len(maps) #가로
    M = len(maps[0]) #세로
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
    #Start위치 찾기
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='S':
                q.append((i,j,0))
                dist[i][j]=0
            if q:
                break
    while q:
        x,y,c =q.popleft()
        #레버 위치 찾기
        if maps[x][y]=='L':
            return c
        #네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            n_x = x
            n_y = y
            
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<= n_x+dx[i]<N and 0<=n_y+dy[i]<M and maps[n_x+dx[i]][n_y+dy[i]] != 'X':
                n_x += dx[i]
                n_y += dy[i]
            # 이전에 해당 위치에 도달한 적이 없거나 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[n_x][n_y] >c+1:
                dist[n_x][n_y] = c+1
                q.append((n_x, n_y, c+1))
    return -1
# 미로탈출
from collections import deque

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False]*m for _ in range(n)]
    que = deque()
    flag = False
    
    # 초깃값 설정
    for i in range(n):
        for j in range(m):
        	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                visited[i][j] = True
                flag = True; break 
                # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
        if flag: break
                
    # BFS 알고리즘 수행 (핵심)
    while que:
        y, x, cost = que.popleft()
        
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0<= ny <n and 0<= nx <m and maps[ny][nx] !='X':
                if not visited[ny][nx]:	# 아직 방문하지 않는 통로라면
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1	# 탈출할 수 없다면
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1

# 호텔 대실 : 예제 테스트는 성공 but 정확도 15.3,,,
def solution(book_time):
    new_book_time = []
    room = []
    for i in book_time:
        a, b = map(int,i[0].split(':'))
        c, d = map(int,i[1].split(':'))
        new_book_time.append([a*60+b, c*60+d+10])
    new_book_time.sort(key=lambda x:x[0])
    if new_book_time:
        for i in new_book_time:
            if room:
                for j in room:
                    if j[1]<=i[0]:
                        room.remove(j)
            room.append(i)
    return len(room)
# 호텔 대실 : 여러 예약이 겹칠 수 있으므로 break를 넣어줌으로써 해결!
def solution(book_time):
    new_book_time = []
    room = []
    for i in book_time:
        a, b = map(int,i[0].split(':'))
        c, d = map(int,i[1].split(':'))
        new_book_time.append([a*60+b, c*60+d+10])
    new_book_time.sort(key=lambda x:x[0])
    if new_book_time:
        for i in new_book_time:
            if room:
                for j in room:
                    if j[1]<=i[0]:
                        room.remove(j)
                        break
            room.append(i)
    return len(room)

#무인도 여행 : 왜 안되지,,,
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    sol = []
    n = len(maps)
    m = len(maps[0])
    check = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if check[i][j]==False and maps[i][j] != 'X':
                check[i][j]=True
                answer += int(maps[i][j])
                for k in range(4): 
                    n_x = i
                    n_y = j
                    while 0 <= n_x+dx[k]<n and 0<= n_y+dy[k]<m and maps[n_x+dx[k]][n_y+dy[k]] != 'X' and check[n_x+dx[k]][n_y+dy[k]] == False:
                        n_x += dx[k]
                        n_y += dy[k]
                        answer += int(maps[n_x][n_y])
                        check[n_x][n_y]= True
            sol.append(answer)
            answer = 0
    return sol
# 무인도 여행 chatgpt
from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    sol = []
    que = deque()
    n = len(maps)
    m = len(maps[0])
    check = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not check[i][j]:
                check[i][j] = True
                answer += int(maps[i][j])
                que.append((i, j))
                while que:
                    cur_x, cur_y = que.popleft()
                    for o in range(4):
                        n_x, n_y = cur_x + dx[o], cur_y + dy[o]
                        if 0 <= n_x < n and 0 <= n_y < m and maps[n_x][n_y] != 'X':
                            if not check[n_x][n_y]:
                                answer += int(maps[n_x][n_y])
                                check[n_x][n_y] = True
                                que.append((n_x, n_y))
                sol.append(answer)
                answer = 0
    
    return sorted(sol)

#무인도여행 mine
from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    sol = []
    que = deque()
    n = len(maps)
    m = len(maps[0])
    check = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and not check[i][j]:
                check[i][j]=True
                answer += int(maps[i][j])
                que.append((i,j))
                while que:
                    n_x, n_y = que.popleft()
                    for o in range(4):
                        n_x += dx[o]
                        n_y += dy[o]
                        if 0<= n_x <n and 0<= n_y <m and maps[n_x][n_y] !='X':
                            if not check[n_x][n_y]:
                                answer+=int(maps[n_x][n_y])
                                check[n_x][n_y]=True
                                que.append((n_x,n_y))
                sol.append(answer)
                answer=0
    return sol

# 뒤에 있는 큰 수 찾기 : 시간초과
def solution(numbers):
    result=[]
    for i in range(len(numbers)):
        check=False
        for j in numbers[i+1:]:
            if j > numbers[i]:
                result.append(j)
                check=True
                break
        if check == False:
            result.append(-1)
    return result
            