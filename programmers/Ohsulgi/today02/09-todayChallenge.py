# [PGS] ad 제거하기/09/오슬기

def solution(strArr):
    answer = [i for i in strArr if 'ad' not in i]
    return answer