# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    # 문자 길이에 대한 s 값을 활용하여 파이썬의 슬라이스 기능 사용
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]