# [PGS] n보다 커질 때까지 더하기/06/오슬기

def solution(numbers, n):
    result = 0
    for i in numbers:
        result += i
        if result > n:
            return result