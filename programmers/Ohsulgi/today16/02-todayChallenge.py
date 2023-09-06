'''
[BOJ] 15818 오버플로우와 모듈러/02/오슬기

문제에 적힌 ((a % m) * (b % m)) % m 을 누적으로 구하기 위해
result의 초기값을 1로 할당해야 한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 1
for i in range(n):
    result *= arr[i] % m

print(result % m)