'''
[BOJ] 17945 통학의 신/02/오슬기

2차방정식 근의 공식을 사용한 뒤 int형을 바꿔준다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

x = (-1*2*a + ((2*a)**2 - (4*b))**0.5) / 2
y = (-1*2*a - ((2*a)**2 - (4*b))**0.5) / 2

if x > y:
    print(int(y), int(x))
elif x < y:
    print(int(x), int(y))
else:
    print(int(x))