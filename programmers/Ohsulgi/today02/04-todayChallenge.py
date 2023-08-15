# [PGS] 배열에서 문자열 대소문자 변환하기/04/오슬기

def solution(strArr):
    answer = [strArr[i].upper() if i % 2 == 1 else strArr[i].lower() for i in range(len(strArr))]
    return answer