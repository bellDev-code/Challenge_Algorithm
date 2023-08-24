'''
[PGS] 문자열 내 마음대로 정렬하기/04/오슬기

sorted() 함수는 정렬할 조건을 지정할 수 있다
lambda 함수를 이용하면 조건을 여러개 지절할 수 있다

'''

def solution(strings, n):
    answer = sorted(strings, key= lambda x : (x[n], x))
    return answer