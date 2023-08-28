'''
[BOJ] 14909 양수 개수 세기/05/오슬기

0은 양의 정수가 아니다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

arr = list(map(int, input().split()))

cnt = [i for i in arr if i > 0]
print(len(cnt))