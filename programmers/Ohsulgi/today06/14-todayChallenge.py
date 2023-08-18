# [PGS] 분수의 덧셈/14/오슬기

def solution(numer1, denom1, numer2, denom2):
    import math
    gcd_denom = math.gcd(denom1, denom2)

    denom = gcd_denom * int(denom1 / gcd_denom) * int(denom2 / gcd_denom)
    number = int(denom / denom1) * numer1 + int(denom / denom2) * numer2

    gcd_result = math.gcd(number, denom)
    if gcd_result == 1:
        answer = [number, denom]
    else:
        answer = [int(number / gcd_result), int(denom / gcd_result)]
    return answer