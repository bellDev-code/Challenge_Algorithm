'''
[BOJ] 17496 스타후르츠/01/오슬기

n // t 를 하게되면 0일부터 계산되므로
(n - 1) // t를 해야한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, t, c, p = map(int, input().split())

result = ((n-1) // t) * c * p
print(result)