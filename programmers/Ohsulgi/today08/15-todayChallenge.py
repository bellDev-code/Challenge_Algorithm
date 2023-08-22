'''
[PGS] 2차원으로 만들기/15/오슬기

num_list의 원소를 n개 단위로 슬라이싱해서 리스트에 넣고 answer 리스트에 할당한다

'''

def solution(num_list, n):
    answer = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    return answer