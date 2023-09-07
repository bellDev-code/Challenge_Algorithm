'''
[BOJ] 15921 수찬은 마린보이야!!/02/오슬기

균일한 확률로 뽑을때의 기댓값은 각각의 값을 원소의 개수로 나눈 값이다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print('divide by zero')
else:
    avg = sum(arr) / len(arr)
    exv = [i/len(arr) for i in arr]
    print(f'{avg / sum(exv):.2f}')