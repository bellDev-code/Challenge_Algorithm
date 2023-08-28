'''
[BOJ] 14568 2017 연세대학교 프로그래밍 경시대회/03/오슬기

각각 1개 이상씩 나눠가져야 하므로 1부터 n-2까지이며
영훈은 남규보다 2개 이상 가져야 하므로 남규는 1부터 n-4까지, 영훈은 3부터 n-2까지,
택희는 2부터 n-2까지 짝수만 검사하도록 범위를 설정한다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())

cnt = 0
for i in range(1,n-4):
    for j in range(i+2,n-2):
        for k in range(2,n-2,2):
            if i + j + k == n:
                cnt += 1

print(cnt)