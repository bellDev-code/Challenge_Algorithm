# [PGS] 세 개의 구분자/07/오슬기

def solution(myStr):
    answer = [k for i in myStr.split('a') for j in i.split('b') for k in j.split('c') if k != '']
    
    if len(answer) > 0:
        return answer
    else:
        return ['EMPTY']