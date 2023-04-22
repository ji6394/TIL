# 크레인 인형뽑기 게임
def solution(board, moves):
    bucket = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1]!=0:
                bucket.append(j[i-1])
                j[i-1]=0
                try:
                    if bucket[-1]==bucket[-2]:    
                        answer+=2
                        bucket.pop()
                        bucket.pop()
                finally:
                    break
    return answer

# 키패드 누르기
def distance(num, now_l, now_r, pos, handed):
    x, y = 0, 1
    # 절댓값을 이용해서 거리 구함. x좌표와 y좌표를 각각 계산하여 더함
    dist_l = abs(pos[now_l][x]- pos[num][x]) + abs(pos[now_l][y] - pos[num][y])
    dist_r = abs(pos[now_r][x]- pos[num][x]) + abs(pos[now_r][y] - pos[num][y])
    # 거리가 같을 때
    if dist_l == dist_r:
        return 'R' if handed=='right' else 'L'
    return 'R' if dist_r < dist_l else 'L'
def solution(numbers, hand):
    position = {1 : [0,0], 2 : [0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    left = [1,4,7]
    right = [3,6,9]
    now_l = '*'
    now_r = '#'
    result = ''
    for num in numbers:
        if num in left:
            result += 'L'
            now_l = num
        elif num in right:
            result += 'R'
            now_r = num
        else:
            result += distance(num, now_l, now_r, position, hand)
            if result[-1] == 'L':
                now_l = num
            else:
                now_r = num
    return result

#신규 아이디 추천
import re
def solution(new_id):
    #대문자를 소문자로 변경
    new_id = new_id.lower()
    
    #소문자,숫자,빼기,밑줄,마침표 제외 제거
    lvl2 = re.compile('[0-9a-z_.\-]+') #해당 하는 문자
    new_id = lvl2.findall(new_id)
    new_id=''.join(new_id)
    
    #연속된 . 제거
    while '..' in new_id:
        new_id = new_id.replace('..','.')
        
    # 처음이나 끝에 .?
    new_id = new_id.strip('.')
    
    #빈문자열 a 추가
    if new_id=='':
        new_id += 'a'
    
    #16자 이상일경우 문자 제거
    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    
    #2자 이하일 경우 마지막 문자 복사
    if len(new_id)<=2:
        size = len(new_id)
        addchar = new_id[size-1:]
        while len(new_id)<3:
            new_id+=addchar
    answer = new_id
    return answer