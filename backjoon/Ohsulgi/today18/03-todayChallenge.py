'''
[BOJ] 16503 괄호 없는 사칙연산/03/오슬기

타입 변환을 하지 않고 리스트로 할당하면 모든 원소가 str로 들어간다
0, 2, 4번 인덱스는 int로 변환하고 1, 3번 인덱스의 연산자를 판별하여 연산을 진행한다
연산 순서를 반대로 하는 것이 리스트를 reverse 하는것이 아님에 주의

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

arr = list(input().split())

def cal(arr):
    if arr[1] == '+':
        result = int(arr[0]) + int(arr[2])
    elif arr[1] == '-':
        result = int(arr[0]) - int(arr[2])
    elif arr[1] == '*':
        result = int(arr[0]) * int(arr[2])
    else:
        if int(arr[0]) < 0 or int(arr[2]) < 0:
            result = -1 * (abs(int(arr[0])) // abs(int(arr[2])))
        else:
            result = abs(int(arr[0])) // abs(int(arr[2]))
    return result

cal1 = cal([cal(arr[0:3])] + arr[3:])
cal2 = cal(arr[:2] + [cal(arr[2:])])

print(min(cal1, cal2))
print(max(cal1, cal2))