# 공배수
# 삼항연산자 방법으로 해결
# 공배수는 n, m의 배수인 수를 말한다.
# if문 조건문을 두 개 할당 하기 위해서 and 활용하였음
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0