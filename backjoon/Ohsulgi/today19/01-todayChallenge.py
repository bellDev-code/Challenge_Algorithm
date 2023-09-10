'''
[BOJ] 17174 전체 계산 횟수/01/오슬기

묶음이 1개가 될때까지 반복해야 하므로 while문을 이용한다
마지막 남은 묶음도 포함하는 것에 유의

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

result = n
group = n
while group > 1:
    a = group // m
    result += a
    group = a

print(result)