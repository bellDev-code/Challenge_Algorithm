# [PGS] 저주의 숫자 3/19/오슬기

def solution(n):
    answer = [i for i in range(1, 200) if i % 3 != 0 and '3' not in str(i)]
    return answer[n-1]