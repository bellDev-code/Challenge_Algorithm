'''
[PGS] 덧칠하기/01/오슬기

0번 인덱스부터 칠할 필요가 없기 때문에 시작점을 section[0]-1 부터 m만큼 칠한다
다음 인덱스가 이미 칠한 영역이면 pass하고 아니면 반복한다

'''

def solution(n, m, section):
    count = 0
    paint = section[0]-1
    for i in section:
        if i > paint:
            paint = i+m-1
            count += 1
    return count