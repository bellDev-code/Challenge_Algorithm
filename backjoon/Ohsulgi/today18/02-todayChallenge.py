'''
[BOJ] 16483 접시 안의 원/02/오슬기

작은 원의 접선은 직선 T와 수직을 이루고
접선과 큰 원이 만나는 점은 큰 원의 반지름의 길이를 가진 사선으로
직각 삼각형을 이루므로 피타고라스 정리 사용 가능

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

t = int(input())
print(int(round((t/2)**2, 0)))