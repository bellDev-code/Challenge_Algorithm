'''
[PGS] 가장 큰 수 찾기/10/오슬기

max() 함수는 인자들 중 제일 큰 값을 출력
list.index() 는 인자의 리스트 내 인덱스를 출력

'''

def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer