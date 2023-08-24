'''
[PGS] 가장 가까운 같은 글자/07/오슬기

s의 i번째 인덱스로 슬라이싱 한 뒤 i번째 글자가 s[:i] 안에 있으면
역순으로 정렬한 뒤 거리를 출력하고 없으면 -1을 출력한다

'''

def solution(s):
    answer = []; [answer := answer + [-1 if s[i] not in s[:i] else len(s[:i][::-1][0:s[:i][::-1].index(s[i])+1])] for i in range(len(s))]
    return answer