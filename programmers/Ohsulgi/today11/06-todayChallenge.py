'''
[PGS] 폰켓몬/06/오슬기

set 자료형은 중복을 제거하므로 list(set(list()))의 형태로 중복을 제거한 리스트로 만들 수 있다

'''

def solution(nums):
    set_nums = list(set(nums))

    if len(set_nums) >= int(len(nums) / 2):
        return len(set_nums[:int(len(nums) / 2)])
    else:
        return len(set_nums)