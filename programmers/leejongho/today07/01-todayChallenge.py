# 조건 문자열
# 정수의 크기, ineq의 모양에 따라 if문의 조건문을 생각했습니다.
# if문의 and 조건을 통해 최대한 같은 조건을 찾았습니다.
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq == ">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer
