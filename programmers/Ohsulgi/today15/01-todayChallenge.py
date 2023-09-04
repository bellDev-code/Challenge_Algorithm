'''
[BOJ] 14913 등차수열에서 항 번호 찾기/01/오슬기

등차수열인지 확인하려면 (확인하려는 항 - 첫째 항) % 등차 가 0 뿐만 아니라
(확인하려는 항 - 첫째 항) / 등차 가 0보다 큰지도 확인해야 한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

a, d, k = map(int, input().split())

x, y = divmod((k-a), d)
if x < 0 or y != 0:
    print('X')
else:
    print((k-a) // d + 1)