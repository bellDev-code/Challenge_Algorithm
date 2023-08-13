# [PGS] 수열 구간 쿼리 1/07/오슬기

def solution(arr, queries):
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1]+1):
            arr[j] +=1
    return arr