'''
[PGS] 예산/12/오슬기

예산을 남기지 말라는 조건은 없으니 예산에 맞추기 위해 다른 조합을 찾지 않아도 된다
오름차순으로 정렬 후 예산 안에서 최대의 수만 찾으면 된다

'''

def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if i > budget:
            break
        budget -= i
        answer += 1
    return answer