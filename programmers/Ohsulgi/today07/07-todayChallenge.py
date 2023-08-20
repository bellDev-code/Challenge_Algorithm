'''
[PGS] n의 배수 고르기/07/오슬기

n의 배수 = n으로 나눴을 때 나머지가 0 이므로
numlist에서 n으로 나눴을 때 나머지가 0인 원소들만 answer에 추가

'''

def solution(n, numlist):
    answer = [i for i in numlist if i % n == 0]
    return answer