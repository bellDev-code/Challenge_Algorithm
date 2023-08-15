# [PGS] 배열의 길이를 2의 거듭제곱으로 만들기/12/오슬기

def solution(arr):
    i = 0
    while 2**i < len(arr):
        i += 1

    for _ in range(2**i - len(arr)):
        arr.append(0)
    return arr