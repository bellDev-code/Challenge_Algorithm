'''
[PGS] 세균 증식/03/오슬기

첫째항 n 과 공비 2, 항의 개수 t로 이루어진 등비수열

'''

def solution(n, t):
    answer = n * (2 ** t)
    return answer