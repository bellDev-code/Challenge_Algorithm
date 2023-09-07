'''
[BOJ] 15780 멀티탭 충분하니?/05/오슬기

한 칸을 띄워 꼽아야 하기 때문에 n구의 멀티탭에는
n / 2를 반올림한 값만큼 사용할 수 있다. 

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    result += int(round(i / 2 + 0.0001, 0))

if result >= n:
    print('YES')
else:
    print('NO')