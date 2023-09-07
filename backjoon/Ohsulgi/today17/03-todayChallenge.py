'''
[BOJ] 16431 베시와 데이지/03/오슬기

daisy는 대각선 이동을 못하므로 john과의 x, y좌표의 차이만큼이 걸린 시간이 되지만
bessie는 대각선 이동이 가능하므로 x, y중 어느 한 곳의 상대좌표가 0이 될때까지 while문을
돌리고 그 다음 0이 아닌 좌표의 차이만큼 더한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

bessie = list(map(int, input().split()))
daisy = list(map(int, input().split()))
john = list(map(int, input().split()))

time_daisy = abs(daisy[0] - john[0]) + abs(daisy[1] - john[1])

john_to_bessie = [abs(bessie[0] - john[0]), abs(bessie[1] - john[1])]
time_bessie = 0
while True:
    if john_to_bessie[0] == 0 or john_to_bessie[1] == 0:
        break
    john_to_bessie[0] -= 1
    john_to_bessie[1] -= 1
    time_bessie += 1
time_bessie += john_to_bessie[0] + john_to_bessie[1]

if time_bessie < time_daisy:
    print('bessie')
elif time_bessie > time_daisy:
    print('daisy')
else:
    print('tie')