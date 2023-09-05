'''
[PGS] 다음 큰 숫자/06/오슬기

n+1 부터 2진수로 변환시켜 리스트로 만든 뒤 1의 개수를 세어
n과 같을 때 출력한다

'''

def solution(n):
    cnt = n+1
    while True:
        if list(str(bin(cnt)[2:])).count('1') == list(str(bin(n)[2:])).count('1'):
            break
        cnt += 1
    return cnt