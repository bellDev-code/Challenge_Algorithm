'''
[PGS] 중복된 문자 제거/02/오슬기

문자열의 공백까지 리스트의 요소로 추가한 뒤 딕셔너리에
요소가 처음 나오면 값을 추가하고 중복된 요소는 무시

'''

def solution(my_string):
    str_list = list(my_string)

    str_dict = {}
    for i in str_list:
        if i not in str_dict:
            str_dict[i] = 1
        else:
            pass

    answer = ''.join(str_dict.keys())
    return answer