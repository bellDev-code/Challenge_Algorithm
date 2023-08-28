'''
[PGS] 이진 변환 반복하기/08/오슬기

s에서 0의 개수와 1의 개수를 각각 카운트해서
0의 개수는 따로 집계하고 1의 개수를 2진수로 변환해서 s에 저장한다

'''

def solution(s):
    change, number0 = 0, 0
    while True:
        if s == '1':
            break
        s_list = list(s)
        number0 += s_list.count('0')
        s = str(bin(s_list.count('1'))[2:])
        change += 1
    return [change, number0]