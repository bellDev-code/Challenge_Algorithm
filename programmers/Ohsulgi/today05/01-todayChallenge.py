# [PGS] 주사위 게임 1/01/오슬기

def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        answer = a**2 + b**2
        return answer
    elif a % 2 == 1 or b % 2 == 1:
        answer = 2 * (a + b)
        return answer
    else:
        answer = abs(a - b)
        return answer