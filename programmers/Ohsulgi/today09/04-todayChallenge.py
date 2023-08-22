'''
[PGS] 369게임/04/오슬기

int를 각 자리별로 리스트에 할당하려면 str로 변환 후 해야함
order의 원소가 3,6,9에 해당하면 answer에 1 추가

'''

def solution(order):
    order_list = list(str(order))
    answer = 0
    for i in order_list:
        if int(i) in [3, 6, 9]:
            answer += 1
    return answer