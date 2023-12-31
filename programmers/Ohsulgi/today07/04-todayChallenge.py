'''
[PGS] 제곱수 판별하기/04/오슬기

1 <= n <= 1000000 이고 1000000 ** (1/2) == 1000 이므로
1부터 1000까지 반복문을 돌려 n이 해당되는지 검사

'''

def solution(n):
    for i in range(1,1001):
        if i ** 2 == n:
            return 1
    return 2