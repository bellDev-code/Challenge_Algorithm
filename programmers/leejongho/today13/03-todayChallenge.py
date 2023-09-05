# n보다 커질 때 까지 구하기
def solution(numbers, n):
    result = 0
    el = 0
    
    for num in numbers:
        el += num
        if el > n:
            break
    result = el
    return result