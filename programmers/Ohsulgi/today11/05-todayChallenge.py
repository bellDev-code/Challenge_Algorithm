'''
[PGS] 카드 뭉치/05/오슬기

goal의 문자열과 cards1, cards2의 0번 인덱스를 비교해서
해당되는게 없으면 No를 출력하고 있다면 그 리스트의 0번 인덱스를 삭제한다

'''

def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and i == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'