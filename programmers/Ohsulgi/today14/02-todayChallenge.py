'''
[BOJ] 25630 팰린드롬 소떡소떡/02/오슬기

문자열과 뒤집은 문자열을 비교하여 다른 문자열이 있으면 카운트를 1씩 증가한다
문자열의 중간이 지나는 부분부터는 이미 검사하였으므로 문자열의 중간 인덱스까지만 검사

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

n = int(input().rstrip())

st_list2 = list(input().rstrip())
st_list3 = st_list2.copy()[::-1]

cnt = 0
for i in range(int(len(st_list2) / 2)):
    if st_list2[i] != st_list3[i]:
        cnt += 1
print(cnt)