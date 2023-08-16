# [PGS] 문자열 정수의 합/08/오슬기

def solution(num_str):
    arr = list(map(int, list(num_str)))
    return sum(arr)