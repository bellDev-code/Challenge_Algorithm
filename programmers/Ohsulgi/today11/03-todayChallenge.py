'''
[PGS] 명예의 전당 (1)/03/오슬기

for문을 돌려서 순차적으로 원소를 추가한 뒤 내림차순으로 정렬하여
-1번 인덱스를 answer 리스트에 추가한다

'''

def solution(k, score):
    result, answer = [], []
    for i in score:
        result.append(i)
        result.sort()
        answer.append(result[::-1][:k][-1])
    return answer