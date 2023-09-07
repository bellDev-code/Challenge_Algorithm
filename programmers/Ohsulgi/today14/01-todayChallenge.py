'''
[BOJ] 23812 골뱅이 찍기 - 돌아간 ㅍ/01/오슬기

가로축으로 문자열이 늘어나면 * N
세로축으로 문자열이 늘어나면 for문을 N번 반복

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)
for _ in range(n):
    print('@'*5*n)
for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)
for _ in range(n):
    print('@'*5*n)
for _ in range(n):
    print('@'*n + ' '*3*n + '@'*n)