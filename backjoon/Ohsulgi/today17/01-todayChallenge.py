'''
[BOJ] 15917 노솔브 방지문제야!!/01/오슬기

a가 2의 거듭제곱꼴인지 확인할 때 매번 for문으로 확인한다면
확인한 값을 다시 확인해야하기 때문에 시간도 오래걸리고 비효율적이다
딕셔너리는 시간복잡도가 O(1)인 해시함수이므로 미리 저장해놓고 비교하면 효율적이다

'''

import sys
sys.stdin = open('D:\data\백준\input.txt', 'r')
input = sys.stdin.readline

dict_ = {i:2**i for i in range(31)}

for _ in range(int(input())):
    a = int(input())
    if a in dict_.values():
        print(1)
    else:
        print(0)