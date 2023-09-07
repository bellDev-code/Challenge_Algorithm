# n개 간격 원소들
def solution(num_list, n):
    result = []
    for idx, el in enumerate(num_list):
        if idx % n == 0:
            result.append(el)
    return result