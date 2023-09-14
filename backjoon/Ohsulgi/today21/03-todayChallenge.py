'''
[BOJ] 17944 퐁당퐁당 1/03/오슬기

1부터 2*n까지 주기적으로 반복하는 배열을 만들기 위해
direction이 0일때에는 정방향으로 올라가다가 2*n이 되었을 때 방향을 바꾼다
direction이 1일때에는 역방향으로 내려가다가 1이 되었을 때 방향을 바꾼다
cnt가 t가 되었을때 반복문을 중단하고 그때의 값을 출력한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n, t = map(int, input().split())

direction = 0
cnt = 1
number = 1
while True:
    if cnt == t:
        break
    if direction == 0:
        number += 1
        cnt += 1
        if number == 2*n:
            direction = 1
    else:
        number -= 1
        cnt += 1
        if number == 1:
            direction = 0

print(number)