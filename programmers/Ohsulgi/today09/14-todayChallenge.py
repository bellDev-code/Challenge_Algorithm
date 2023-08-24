'''
[PGS] 크기가 작은 부분문자열/14/오슬기

문자열의 i번 인덱스부터 i + p의 길이 만큼
for문을 돌면서 p와 크기를 비교한다

'''

def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer