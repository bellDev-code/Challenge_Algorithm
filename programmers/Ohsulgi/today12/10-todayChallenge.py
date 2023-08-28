'''
[BOJ] 14264 정육각형과 삼각형/10/오슬기

정육각형의 내각은 120도 이므로 문제에서 요구하는 삼각형의 넓이는
넓이 = 정육각형 한 변의 길이 * 루트3 * 삼각형의 높이 / 2

'''

import sys
input = sys.stdin.readline

n = int(input())

answer = n * (3 ** 0.5) * (n / 2) * 0.5
print(answer)