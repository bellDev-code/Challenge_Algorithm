'''
[PGS] k의 개수/11/오슬기

i부터 j까지 모든 숫자를 하나의 문자열로 합친 뒤
k가 몇번 등장하는지 str.count(k)로 출력

'''

def solution(i, j, k):
    arr = ''
    for a in range(i,j+1):
        arr += str(a)
    return arr.count(str(k))