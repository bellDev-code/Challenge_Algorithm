'''
[BOJ] 16673 고려대학교에는 공식 와인이 있다/05/오슬기

c년까지 포함해야 하므로 범위를 1부터 c+1로 정해야 한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

c, k, p =  map(int, input().split())

answer = 0
for i in range(1, c+1):
    answer += (k*i) + (p*(i**2))

print(answer)