'''
[PGS] 외계행성의 나이/07/오슬기

age를 숫자 하나씩 슬라이싱 하여 리스트에 할당한다
chr() 함수는 숫자를 인자로 입력하면 그 숫자에 해당하는 아스키문자를 출력
a의 아스키 코드는 97이므로 chr(슬라이싱한 숫자 + 97)로 원하는 문자 출력 가능

'''

def solution(age):
    age_list = list(str(age))
    answer = [chr(int(i) + 97) for i in age_list]
    return ''.join(answer)