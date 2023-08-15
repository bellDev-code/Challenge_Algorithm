# [PGS] 공백으로 구분하기 2/03/오슬기

def solution(myString):
    myString = myString.split('x')
    answer = [i for i in myString if i != '']
    answer.sort()
    return answer