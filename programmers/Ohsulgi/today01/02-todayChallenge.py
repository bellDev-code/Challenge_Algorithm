# [PGS] n개 간격의 원소들/02/오슬기

def solution(num_list, n):
    arr = []
    for i in range(0, len(num_list), n):
        arr.append(num_list[i])
    return arr