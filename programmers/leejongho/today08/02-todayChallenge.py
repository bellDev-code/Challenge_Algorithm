# 원소들의 곱과 합
def solution(num_list):
    # 초기화
    mul = 1
    total_sum = 0
    
    # 원소들의 곱, 합
    for num in num_list:
        mul *= num
        total_sum += num
    
    if mul < total_sum ** 2:
        return 1
    else:
        return 0