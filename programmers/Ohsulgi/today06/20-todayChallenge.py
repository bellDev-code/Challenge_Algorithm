# [PGS] 유한소수 판별하기/20/오슬기

def solution(a, b):
    import math

    gcd = math.gcd(a, b)

    c = int(a / gcd)
    d = int(b / gcd)

    while d > 1:
        if d % 2 == 0:
            d = int(d / 2)
        elif d % 5 == 0:
            d = int(d / 5)
        else:
            return 2
    return 1