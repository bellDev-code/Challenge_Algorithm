'''
[BOJ] 16504 종이접기/01/오슬기

N * N 배열을 반으로 접는다는 것에 매몰되지 않아야한다
결국 배열의 모든 원소를 더하라는 뜻

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

sum_ = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    sum_ += sum(arr)

print(sum_)