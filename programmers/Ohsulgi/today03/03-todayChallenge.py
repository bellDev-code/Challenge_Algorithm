# [PGS] 문자열 잘라서 정렬하기/03/오슬기

def solution(myString):
    myString = myString.split('x')
    answer = [i for i in myString if i != '']
    answer.sort()
    return answer