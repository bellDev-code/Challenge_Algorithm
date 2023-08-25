'''
[PGS] 최댓값과 최솟값/04/오슬기

map(적용할 함수, iterator)로 사용하며 iterator의 각 요소에 함수를 적용하여 반환한다

'''

def solution(s):
    s_list = list(map(int, s.split()))
    answer = f'{min(s_list)} {max(s_list)}'
    return answer