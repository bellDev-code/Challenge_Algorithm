# [PGS] l로 만들기/06/오슬기

def solution(myString):
    answer = ['l' if ord(i) < ord('l') else i for i in myString]
    return ''.join(answer)