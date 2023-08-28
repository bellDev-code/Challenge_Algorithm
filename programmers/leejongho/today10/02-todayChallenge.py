# 문자열 뒤의 n글자
# my_string = "ProgrammerS123"
# n = 11
def solution(my_string, n):
    # 파이썬 문자열 슬라이싱 방법 활용 음수값은 뒤에서 부터 슬라이싱
    return my_string[-n:]