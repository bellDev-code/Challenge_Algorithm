# 접미사인지 확인하기
# 접미사란 낱말의 끝에 붙여서 의미를 첨가하여 다른 낱말을 이루는 말
# 파이썬 내장함수에 endswith를 활용
# 해당되는 텍스트가 있으면 1 아니면 0을 리턴하는 삼항연산자 활용
def solution(my_string, is_suffix):
    return 1 if my_string.endswith(is_suffix) else 0