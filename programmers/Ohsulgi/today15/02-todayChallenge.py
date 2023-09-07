'''
[BOJ] 14920 3n+1 수열/02/오슬기

특정 범위가 주어지지 않고 어떤 값으로 수렴하거나
발산하는 경우 while을 쓰는 것이 좋다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

c = int(input())
cnt = 1
while True:
    if c == 1:
        break
    if c % 2 == 0:
        c /= 2
        cnt += 1
    else:
        c = 3*c + 1
        cnt += 1

print(cnt)