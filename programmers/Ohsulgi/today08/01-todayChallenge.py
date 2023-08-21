'''
[PGS] 구슬을 나누는 경우의 수/01/오슬기

n개의 구슬 중 a개를 골라 나누어 주는 것은 조합(combination)
math 라이브러리의 comb 메서드를 통해 구할 수 있다

'''

def solution(balls, share):
    import math

    answer = math.comb(balls, share)
    return answer