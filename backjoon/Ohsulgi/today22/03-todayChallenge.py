'''
[BOJ] 18127 모형결정/03/오슬기

n각형일 때 첫째 항은 1이고 공차가 n-2인 등차수열이 된다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

total = 1
for i in range(1, b+1):
    sub = 1+(a-2)*i
    total += sub

print(total)