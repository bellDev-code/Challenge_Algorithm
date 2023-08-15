# [PGS] 문자열 묶기/02/오슬기

def solution(strArr):
    arr = {}
    for i in strArr:
        if len(i) not in arr:
            arr[len(i)] = 1
        else:
            arr[len(i)] += 1
    return max(arr.values())