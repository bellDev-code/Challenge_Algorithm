# [PGS] 특별한 이차원 배열 1/07/오슬기

def solution(n):
    answer = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return answer