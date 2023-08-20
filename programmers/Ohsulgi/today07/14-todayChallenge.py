'''
[PGS] 삼각형의 완성조건 (2)/14/오슬기

sides의 두 원소의 합보다 크거나
두 원소의 차보다 작으면 삼각형이 만들어지지 않음
두 범위 사이의 모든 값의 개수를 구한다

'''

def solution(sides):
    sides.sort()

    max_length = sum(sides) - 1
    min_length = max(sides) - min(sides)
    answer = max_length - min_length
    return answer