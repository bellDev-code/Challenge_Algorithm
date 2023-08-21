'''
[PGS] A로 B 만들기/13/오슬기

before과 after 모두 리스트로 만들어 오름차순으로 정렬
두 리스트가 같으면 before의 순서를 바꿔서 after를 만들 수 있는 것

'''

def solution(before, after):
    before_list = sorted(list(before))
    after_list = sorted(list(after))

    if before_list == after_list:
        return 1
    else:
        return 0