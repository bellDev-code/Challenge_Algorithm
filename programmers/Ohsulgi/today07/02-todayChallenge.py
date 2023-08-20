'''
[PGS] 문자열 정렬하기 (2)/02/오슬기

string.lower()로 전체 문자열 소문자로 변환
리스트에 넣은 뒤 sort()로 알파벳 순으로 정렬

'''

def solution(my_string):
    my_string = list(my_string.lower())
    my_string.sort()
    answer = ''.join(my_string)
    return answer