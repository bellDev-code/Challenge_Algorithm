'''
[PGS] 문자열안에 문자열/05/오슬기

bool(조건) 은 안의 조건에 따라 True, False를 출력

'''

def solution(str1, str2):
    if bool(str2 in str1) == True:
        return 1
    else:
        return 2