'''
[BOJ] 17504 제리와 톰 2/06/오슬기

분자, 분모로 나눈 뒤 각 단계의 계산결과를 저장하고 스왑하여 역수를 표현한다
마지막으로 기약분수를 나타내기 위해 최대공약수로 분자와 분모를 나누어준다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline
import math

n = int(input())
arr = list(map(int, input().split()))[::-1]

a, b = 1, 1
for i in range(n):
    if i == 0:
        b = arr[0]
    else:
        a = b * arr[i] + a
        a, b = b, a
a = b - a

c = math.gcd(a, b)
print(int(a / c), int(b / c))