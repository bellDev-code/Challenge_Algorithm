# [PGS] 특별한 이차원 배열 2/02/오슬기

def solution(arr):
    answer = [True if arr[i][j] == arr[j][i] else False for j in range(len(arr)) for i in range(len(arr))]

    if False in answer:
        return 0
    else:
        return 1