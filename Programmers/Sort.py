#정렬
#K번째수
def solution(array, commands):
    answer=[]
    for i in commands:
        a,b,c = i
        real_array = array[a-1:b]
        real_array.sort()
        num = real_array[c-1]
        answer.append(num)
    return answer