'''
[PGS] 소수 만들기/09/오슬기

소수 판별 함수를 만들고 combinations 메서드로 nums에 있는 숫자들 중 3개를 고르는 순열 리스트를 만든다
각각의 순열 리스트의 합을 소수 판별 함수에 넣어서 소수가 맞으면 +1

'''

def solution(nums):
    def check(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    from itertools import combinations

    arr = list(combinations(nums, 3))

    answer = 0
    for i in arr:
        if check(sum(i)) == True:
            answer += 1
    return answer