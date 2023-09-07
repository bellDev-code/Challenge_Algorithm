'''
[BOJ] 15734 명장 남정훈/04/오슬기

양발잡이의 범위가 100까지이므로 브루트포스로 가능하다
for문으로 L,R에 배분하는 모든 경우를 찾아본다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

l, r, a = map(int, input().split())

arr = [min(l+i, r+(a-i)) * 2 for i in range(a+1)]
print(max(arr))