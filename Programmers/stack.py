def solution(board, moves):
    bucket = []
    for i in moves:
        for j in board:
            if j[i-1]==0:
                continue
            else:
                bucket.append(j[i-1])
    return bucket
                
