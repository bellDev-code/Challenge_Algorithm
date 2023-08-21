'''
[PGS] 팩토리얼/14/오슬기

math.factorial(n)을 이용하여 n!을 구할수 있다

'''

def solution(n):
    import math

    answer = 1
    while True:
        if math.factorial(answer) > n:
            break
        answer += 1
    return answer-1