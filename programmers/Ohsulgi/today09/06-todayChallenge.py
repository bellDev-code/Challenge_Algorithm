'''
[PGS] 피자 나눠 먹기 (2)/06/오슬기

math 라이브러리의 gcd 메서드는 인자들의 최대 공약수를 출력한다
문제에서 총 피자조각은 최대공배수를 의미하므로

최대공배수 = 최대공약수 * (인자1 / 최대공약수) * (인자2 / 최대공약수) 로 구할 수 있다

'''

def solution(n):
    import math

    gcd = math.gcd(n, 6)
    answer = gcd * int(n / gcd) * int(6 / gcd)
    return int(answer / 6)