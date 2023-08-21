'''
[PGS] 소인수분해/05/오슬기

n까지의 모든 소수를 판별하는 함수 pn_check을 이용하여 prime_number 리스트를 만들고
그 안의 요소들로 나누어 떨어지면 소인수이므로 answer에 추가

'''

def pn_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(n):
    prime_number = [i for i in range(2, n+1) if pn_check(i) == True]

    answer = []
    for i in prime_number:
        if n % i == 0:
            answer.append(i)
            n = int(n / i)
    return answer