# [PGS] 길이에 따른 연산/11/오슬기

def solution(arr):
    if len(arr) >= 11:
        return sum(arr)
    else:
        result = 1
        for i in arr:
            result = result * i
        return result