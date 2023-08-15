# [PGS] 배열의 원소만큼 추가하기/08/오슬기

def solution(arr):
    answer = [i for i in arr for j in range(i)]
    return answer