'''
[PGS] 인덱스 바꾸기/09/오슬기

리스트 내 두 인덱스 간의 요소를 치환하려면
list[a], list[b] = list[b], list[a]

'''

def solution(my_string, num1, num2):
    str_list = list(my_string)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    return ''.join(str_list)