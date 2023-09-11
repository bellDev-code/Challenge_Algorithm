'''
[BOJ] 17350 2루수 이름이 뭐야/02/오슬기

일부문자열A in 문자열B 은 B 안에 A가 있으면 기타 다른 문자가 있어도 True이지만
문제에서 요구하는 조건을 만족하려면 A외에 다른 문자가 없는 == 형태를 만족해야한다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

answer = 0
for _ in range(int(input())):
    player = input().rstrip()
    if 'anj' == player:
        answer = 1

if answer == 1:
    print('뭐야;')
else:
    print('뭐야?')