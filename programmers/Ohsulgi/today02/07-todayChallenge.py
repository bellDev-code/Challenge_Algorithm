# [PGS] 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기/07/오슬기

def solution(myString, pat):
    myString = list(myString)[::-1]
    pat = list(pat)[::-1]
    
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            return ''.join(myString[i:][::-1])