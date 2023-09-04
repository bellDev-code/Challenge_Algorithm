'''
[BOJ] 15667 2018 연세대학교 프로그래밍 경진대회/03/오슬기

1개의 대형 폭죽이 k개의 중형 폭죽으로, k개의 중형 폭죽이 k개의 소형 폭죽으로
갈라지면 총 폭죽의 개수는 k**2 + k + 1개이다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())
for i in range(int(n ** 0.5)+1):
    if i ** 2 + i + 1 == n:
        print(i)
        break