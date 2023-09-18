'''
[BOJ] 17618 신기한 수/01/오슬기

정수를 str로 바꿔서 리스트에 할당하면 숫자 하나씩 들어간다
하지만 이대로 sum을 할 수 없으므로 map함수를 이용해 리스트의 원소들을
다시 정수로 바꾸어 재할당한 뒤 더한다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

cnt = 0
for i in range(1, int(input())+1):
    arr = list(map(int, list(str(i))))
    if i % sum(arr) == 0:
        cnt += 1

print(cnt)