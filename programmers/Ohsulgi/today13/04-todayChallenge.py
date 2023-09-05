'''
[BOJ] 14656 조교는 새디스트야!!/04/오슬기

주어진 숫자 배열 앞에 0을 넣고 리스트를 만들면
숫자의 인덱스와 숫자를 직접 비교가 가능해진다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

cnt = 0
for i in range(1,len(arr)):
    if arr[i] != i:
        cnt += 1

print(cnt)