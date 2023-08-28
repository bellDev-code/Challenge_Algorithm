'''
[BOJ] 15904 UCPC는 무엇의 약자일까?/01/오슬기

주어진 문자열 중 타깃으로 하는 U,C,P,C만 모은 뒤
순서대로 UCPC가 있는지 확인한다.

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

str_ucpc = input().rstrip()
target = ['U','C','P','C']

result = ''
for i in range(len(str_ucpc)):
    if str_ucpc[i] in target:
        result += str_ucpc[i]

idx = 0
answer = ''
for x in result:
    if answer == 'UCPC':
        break
    elif x == target[idx]:
        answer += x
        idx += 1

if answer == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')