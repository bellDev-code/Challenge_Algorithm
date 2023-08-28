'''
[BOJ] 14579 덧셈과 곱셈/02/오슬기

1부터 n까지의 합을 for를 이용하면 2중 for문으로 시간이 매우 많이 걸리므로
n(n+1)/2 공식을 사용하면 시간이 많이 단축된다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

answer = 1
for i in range(a, b+1):
    answer *= int((i * (i+1)) / 2)

print(answer % 14579)