'''
[PGS] 콜라 문제/01/오슬기

새 콜라로 바꾼 병과 바꾸지 못한 빈 병을 같이 고려해야 한다
매 단계마다 그 둘을 더해서 바꿀 수 있는 최대값을 구한다

'''

def solution(a, b, n):
    answer = 0
    bottle = n
    while bottle >= a:
        c, d = divmod(bottle, a)
        answer += c * b
        bottle = c * b + d
    return answer