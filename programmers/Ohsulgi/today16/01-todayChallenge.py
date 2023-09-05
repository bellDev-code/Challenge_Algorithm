'''
[BOJ] 15784 질투진서/01/오슬기

n x n 배열을 2차원 array로 만든 뒤 조건에 위치한 값들을 따로 빼내어 비교한다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

jinseo = arr[a-1][b-1]

arr2 = [arr[i][b-1] if arr[i][b-1] > jinseo else max(arr[a-1]) if max(arr[a-1]) > jinseo else 0 for i in range(n)]

if max(arr2) > jinseo:
    print('ANGRY')
else:
    print('HAPPY')