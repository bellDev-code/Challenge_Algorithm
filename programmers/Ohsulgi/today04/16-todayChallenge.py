# [PGS] 꼬리 문자열/16/오슬기/lv0

def solution(str_list, ex):
    answer = [i for i in str_list if ex not in i]
    return ''.join(answer)