# 글자 이어 붙여 문자열 만들기
# my_string = "cvsgiorszzzmrpaqpe"
# index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
def solution(my_string, index_list):
    result = ""
    # for문 활용하여 index_list의 숫자 값에 따라 새로운 문자열에다가 넣어줌
    for index in index_list:
        result += my_string[index]
    return result
        