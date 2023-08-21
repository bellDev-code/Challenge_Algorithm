'''
[PGS] 이진수 더하기/07/오슬기

int(a, b) 함수는 b를 입력하지 않으면 float를 정수로 바꿀 때 주로 사용하지만
b 인자를 입력하면 a를 b진수로 인식하여 10진수로 변환한 값을 출력한다

bin()은 10진수를 2진수로 변환할 때 앞에 0x가 붙으므로 [2:]로 슬라이싱 필요

'''

def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)

    answer = str(bin(a+b)[2:])
    return answer