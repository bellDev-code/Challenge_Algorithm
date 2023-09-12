'''
[BOJ] 17450 과자 사기/03/오슬기

분자와 분모 모두 10봉지를 곱해야 하므로 주어진 두 수를 그대로 비교하는 것과 같다
가격이 500원 이상일 때에만 할인 쿠폰을 고려해 -50 해준 값과 비교한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]

answer = []
for i in range(3):
    if arr[i][0] < 500:
        result = arr[i][1] / arr[i][0]
        answer.append(result)
    else:
        result = arr[i][1] / (arr[i][0] - 50)
        answer.append(result)

if max(answer) == answer[0]:
    print('S')
elif max(answer) == answer[1]:
    print('N')
else:
    print('U')