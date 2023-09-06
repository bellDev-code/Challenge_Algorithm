'''
[BOJ] 15820 맞았는데 왜 틀리죠?/03/오슬기

샘플-테스트를 모두 맞은 경우, 샘플만 맞은 경우, 샘플도 틀린경우, 테스트 케이스가 0인 경우를
모두 if 문으로 처리해야한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

s1, s2 = map(int, input().split())

answer1 = []
for _ in range(s1):
    a, b = map(int, input().split())
    if a != b:
        answer1.append(1)

if s2 != 0:
    answer2 = []
    for _ in range(s2):
        c, d = map(int, input().split())
        if c != d:
            answer2.append(1)

if len(answer1) == 0:
    if s2 != 0:
        if len(answer2) == 0:
            print('Accepted')
        else:
            print('Why Wrong!!!')
    else:
        print('Accepted')
else:
    print('Wrong Answer')