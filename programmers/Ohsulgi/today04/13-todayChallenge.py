# [PGS] 배열의 원소 삭제하기/13/오슬기

def solution(arr, delete_list):
    answer = [i for i in arr if i not in delete_list]
    return answer