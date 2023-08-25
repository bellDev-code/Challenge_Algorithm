# 수 조작하기 1
# 해당 문자와 정수를 가진 딕셔너리 형태를 구현하여 for문을 활용하여 해당 정수를 더했습니다.
def solution(n, control):
    dic = {"w": 1, "s": -1, "d": 10, "a": -10}
    for str in control:
        n += dic[str]
    return n