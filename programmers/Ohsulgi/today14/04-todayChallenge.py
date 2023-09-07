'''
[BOJ] 15781 헬멧과 조끼/04/오슬기

max() 함수는 주어진 인자 중 최대값을 출력한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(max(arr1) + max(arr2))