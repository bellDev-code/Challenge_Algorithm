# 홀수 vs 짝수

# num_list = [4, 2, 6, 1, 7, 6], result = 17
# num_list = [-1, 2, 5, 6, 3], result = 8
def solution(num_list):
    # 배열 슬라이싱 활용 [start:end] [start:end:step]
    # sum 함수로 배열의 값들 합 확인
    odd_sum = sum(num_list[::2])
    even_sum = sum(num_list[1::2])

    return max(odd_sum, even_sum)