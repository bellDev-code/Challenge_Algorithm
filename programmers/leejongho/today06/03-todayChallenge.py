# 홀짝에 따라 다른 값 반환하기
# n이 홀수와 짝수 일때 구별하여 조건문 작성
def solution(n):
    result = 0
    if n % 2 == 1:
        # range(A, B, C) A부터 C숫자만큼의 간격(1의간격)으로 B-1 까지의 정수 범위를 반환
        for i in range(1, n + 1, 2):
            result += i
    else:
        for i in range(2, n + 1, 2):
            result += i ** 2
    return result