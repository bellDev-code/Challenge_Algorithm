'''
[PGS] 진료 순서 정하기/09/오슬기

응급도를 기준으로 내림차순 정렬한 배열을 생성
emergency의 각 원소를 돌며 배열의 몇 번째 인덱스인지 확인하여 answer에 할당

'''

def solution(emergency):
    order = sorted(emergency)[::-1]
    answer = [order.index(i)+1 for i in emergency]
    return answer