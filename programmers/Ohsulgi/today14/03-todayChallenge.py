'''
[BOJ] 15923 욱제는 건축왕이야!!/03/오슬기

격자에 맞춰서 직각으로 이루어진 도형은 x좌표와 y좌표의
최대 - 최소 값으로 이루어진 직사각형의 둘레와 같다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

x_list, y_list = [], []
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in x_list:
        x_list.append(x)
    if y not in y_list:
        y_list.append(y)

answer = 2*(max(x_list) - min(x_list)) + 2*(max(y_list) - min(y_list))
print(answer)