'''
[PGS] 삼총사/13/오슬기

itertools 라이브러리의 combinations 메서드는 조합을 출력할 수 있다
3명을 합해서 0인 조합을 찾아야 하므로
리스트의 원소 중 3개를 고르는 조합 중 for문을 돌려서
합이 0인것을 찾았을 때 count를 증가시킨다

'''

def solution(number):
    from itertools import combinations

    arr = list(combinations(number, 3))

    answer = 0
    for i in arr:
        if sum(i) == 0:
            answer += 1
    return answer