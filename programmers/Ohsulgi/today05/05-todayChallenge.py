# [PGS] 조건에 맞게 수열 변환하기 3/05/오슬기

def solution(arr, k):
    if k % 2 == 1:
        answer = list(map(lambda x: x*k, arr))
    else:
        answer = list(map(lambda x: x+k, arr))
    return answer