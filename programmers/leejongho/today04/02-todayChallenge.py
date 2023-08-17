# 문자열 섞기
def solution(str1, str2):
    result = ''
    for str1, str2 in zip(str1, str2):
        result += str1 + str2
    return result

# 파이썬 zip 함수를 통한 데이터 엮기