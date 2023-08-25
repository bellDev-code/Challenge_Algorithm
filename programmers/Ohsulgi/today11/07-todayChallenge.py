'''
[PGS] 과일 장수/07/오슬기

score를 내림차순으로 정렬한 뒤 m번 인덱스부터 시작해서
m 씩 떨어진 값들을 출력하여 가격을 계산한다

'''

def solution(k, m, score):
    score = sorted(score)[::-1]

    answer = 0
    for i in range(m, ((len(score) // m) * m)+1, m):
        answer += score[i-1] * m
    return answer