# [PGS] 잘라서 배열로 저장하기/10/오슬기

def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0,len(my_str),n)]
    return answer