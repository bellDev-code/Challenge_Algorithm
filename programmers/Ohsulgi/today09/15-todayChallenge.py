'''
[PGS] 최소직사각형/15/오슬기

2중 리스트의 안쪽 리스트와 바깥쪽 리스트를 모두 정렬한 뒤
0번 인덱스에 해당하는 원소들 중 최대값과
1번 인덱스에 해당하는 원소들 중 최대값을 곱한다

'''

def solution(sizes):
    for i in sizes:
        i.sort()
    sizes.sort()

    x, y = 0, 0
    for j in sizes:
        if j[0] > x:
            x = j[0]
        if j[1] > y:
            y = j[1]
    return x * y