'''
[BOJ] 13416 주식 투자/09/오슬기

각각의 날짜에 최대값이 0보다 크다면 더하고 아니면 패스한다

'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sum_ = 0
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if max(a, b, c) >= 0:
            sum_ += max(a, b, c)
    print(sum_)