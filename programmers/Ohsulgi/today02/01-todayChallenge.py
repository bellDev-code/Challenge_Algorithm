# [PGS] 원하는 문자열 찾기/01/오슬기

def solution(myString, pat):
    mystring_ = myString.lower()
    pat_ = pat.lower()

    if pat_ in mystring_:
        return 1
    else:
        return 0