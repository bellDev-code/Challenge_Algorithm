# [PGS] 문자열이 몇 번 등장하는지 세기/08/오슬기

def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            cnt += 1
            
    return cnt