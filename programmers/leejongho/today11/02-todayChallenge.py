# 접두사인지 확인하기
# 접두사란 낱말의 앞에 붙어서 의미를 첨가하여 다른 낱말을 이루는 말
# 파이썬의 내장함수인 startswith를 활용
# 해당 단어가 접두사면 1 아니면 0을 리턴해주는 삼항연산자 활용
def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0