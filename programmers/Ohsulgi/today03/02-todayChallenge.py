# [PGS] 공백으로 구분하기 2/01/오슬기

def solution(myString):
    arr = myString.split('x')
    answer = [len(i) for i in arr]
    return answer