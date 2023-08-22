'''
[PGS] 약수 구하기/05/오슬기

리스트 컴프리헨션에서 if문을 사용할 때 
2항 연산의 경우 [연산 범위 조건]의 형태
3항 연산의 경우 [연산1 조건 else 연산2 범위]의 형태로 작성

'''

def solution(n):
    answer = [i for i in range(1, n+1) if n % i ==0]
    return answer