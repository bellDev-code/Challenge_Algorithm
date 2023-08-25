'''
[PGS] 최솟값 만들기/06/오슬기

2개의 리스트 중 하나는 오름차순으로, 하나는 내림차순으로 정렬하면
i번째 인덱스에 해당하는 값끼리 곱했을 때 최소가 된다

'''

def solution(a,b):
    a = sorted(a)
    b = sorted(b)[::-1]

    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

