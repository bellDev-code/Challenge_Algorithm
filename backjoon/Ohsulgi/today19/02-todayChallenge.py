'''
[BOJ] 17210 문문문/02/오슬기

규칙2에 의해 문을 여는 배열은 0101... 혹은 1010...밖에는 불가능하다
그러므로 N이 6이상이면 규칙 4는 불가능한 조건이 되어버리고
규칙 3은 항상 참인 조건이 된다
따라서 N이 6미만일 때 시작하는 숫자에 따라 둘 중 한가지를 출력한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = int(input())

if n < 6:
    if a == 0:
        arr = [0 if i % 2 == 0 else 1 for i in range(n)]
        for i in range(1,len(arr)):
            print(arr[i])
    else:
        arr = [1 if i % 2 == 0 else 0 for i in range(n)]
        for i in range(1,len(arr)):
            print(arr[i])
else:
    print('Love is open door')