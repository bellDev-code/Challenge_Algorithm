# 주사위 게임2
# 숫자가 두 개 같을때와 하나만 같을때 경우의 수 생각
def solution(a, b, c):
    if a == b and b == c:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif a == b or b == c or a == c:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return a + b + c