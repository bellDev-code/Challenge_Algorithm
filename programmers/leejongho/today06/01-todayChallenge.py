# n의 배수
# 파이썬 코드의 삼항 연산자를 사용하여 문제 해결
# [조건문] ? [참일 경우 value] : [거짓일 경우 value] 자바스크립트 형태이나, 파이썬은 형태가 다름
# [참일 경우 value] if [조건문] else [거짓일 경우 value]
def solution(num, n):
    return 1 if num % n == 0 else 0