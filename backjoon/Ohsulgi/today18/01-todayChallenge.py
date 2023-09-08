'''
[BOJ] 16479 컵라면 측정하기/01/오슬기

문제의 조건이 등변사다리꼴이므로 윗변과 아랫변을 뺀 나머지는 2등분 할 수 있다
그렇게 구한 d3에 피타고라스 정리를 사용

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

k = int(input())
d1, d2 = map(int, input().split())

if d1 == d2:
    print(k**2)
else:
    d3 = (d1 - d2) / 2

    if d3 == int(d3):
        print(k**2 - int(d3)**2)
    else:
        print(k**2 - d3**2)