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