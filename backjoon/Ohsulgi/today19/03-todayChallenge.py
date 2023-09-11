'''
[BOJ] 17263 Sort 마스터 배지훈/03/오슬기

list.sort() 메서드는 시간복잡도가 O(N)이므로
지금 문제와 같이 단일로는 사용할만하지만
for문이나 다른 함수 안에서 사용하게 되면 시간복잡도가 O(N**2)이 되어버리므로
다른 방법을 사용하는 것이 좋다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[-1])