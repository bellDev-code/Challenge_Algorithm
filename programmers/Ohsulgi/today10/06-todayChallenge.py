'''
[PGS] 두 개 뽑아서 더하기/06/오슬기

itertools 라이브러리의 combinations 메서드를 이용해 순열 조합을 추출한다
두 수의 합이 리스트에 없으면 추가한 뒤 오름차순으로 정렬한다


> 리스트 컴프리헨션에서 self 옵션 사용법

기존의 컴프리헨션에서는 list = [i for i in range() if i not in list] 와 같이
스스로를 체크하는 조건을 사용하지 못하지만
list = []; [list := list + 컴프리헨션 문법] 을 사용하면 가능해진다

'''

def solution(numbers):
    from itertools import combinations

    arr = list(combinations(numbers, 2))
    answer = []; [answer := answer + [sum(i)] for i in arr if sum(i) not in answer]
    answer.sort()
    
    return answer