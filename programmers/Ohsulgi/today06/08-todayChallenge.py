# [PGS] 종이 자르기/08/오슬기

def solution(m, n):
    arr1 = [i for i in range(1,m)]
    arr2 = [i for i in range(1,n)]

    answer = len(arr1) + (m * len(arr2))
    return answer