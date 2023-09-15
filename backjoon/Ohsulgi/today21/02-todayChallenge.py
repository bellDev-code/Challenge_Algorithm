'''
[BOJ] 17614 369/02/오슬기

한 개의 for문 안에서 369가 들어간 숫자를 찾아내서 문자열로 바꾸고
개수를 세는 것은 입력값이 늘어날 때 너무 많은 시간이 걸리므로
미리 369가 포함된 숫자를 집계하고 그 다음으로 박수의 개수를 계산한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

arr = [str(i) for i in range(int(input())+1) if '3' in str(i) or '6' in str(i) or '9' in str(i)]

clap = 0
for i in arr:
    clap += i.count('3')
    clap += i.count('6')
    clap += i.count('9')

print(clap)