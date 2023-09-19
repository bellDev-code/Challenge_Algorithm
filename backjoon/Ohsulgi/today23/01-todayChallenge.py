'''
[BOJ] 18247 겨울왕국 티켓 예매/01/오슬기

알파벳 L은 12번째 글자이므로 n이 12보다 작거나 m이 4보다 작으면 L4석은 존재하지 않는다
또한 L4석은 L열의 4번째 자리가 고정이므로 윗줄의 모든 좌석 + 4를 하면 구할 수 있다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    if n < 12 or m < 4:
        print(-1)
    else:
        print(11*m + 4)