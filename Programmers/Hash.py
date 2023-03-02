#해시
#완주하지 못한 선수
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]
# 위 코드를 돌리니 효율성에서 통과하지 못함
# 해시 알고리즘에 대해 공부해보자
from collections import Counter
def solution(participant, completion):
    p_c = Counter(participant)
    c_c = Counter(completion)
    for i in p_c:
        if p_c[i] != c_c[i]:
            return i
# Counter 라이브러리 유용함
# 해시 : 임의 길이 데이터를 암호화된 고정 길이 데이터로 매핑
# 해시 테이블 : key를 해시 함수에 넣어 얻은 해시 값을 index로 사용하는 데이터 구조
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
    