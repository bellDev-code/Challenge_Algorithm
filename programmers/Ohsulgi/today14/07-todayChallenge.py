'''
[BOJ] 28358 생일 맞추기/06/오슬기

매 월에 해당하는 날짜를 딕셔너리에 저장하면 if문을 많이 줄일 수 있다
월과 일 사이에 공백이 없으면 11월 1일과 1월 11일같이 중복되어 생략될 수 있다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    day = [str(i) for i in range(10) if arr[i] == 1]

    cnt = 0
    day_str = {str(i) + ' ' + str(j) : 0 for i in range(1, 13) for j in range(1, month[i]+1)}

    for i in day_str.keys():
        for j in day:
            if j in i:
                day_str[i] = 1

    print(list(day_str.values()).count(0))