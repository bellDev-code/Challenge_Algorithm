# [PGS] 최빈값 구하기/16/오슬기

def solution(array):
    count = {i:0 for i in range(1000)}
    for j in array:
        count[j] += 1

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    if count[0][1] == count[1][1]:
        return -1
    else:
        return count[0][0]