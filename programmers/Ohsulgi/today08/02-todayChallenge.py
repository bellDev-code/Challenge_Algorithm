'''
[PGS] 문자열 계산하기/02/오슬기

연산 기호는 두 숫자 사이에 존재하므로 배열로 바꿨을 때
짝수 인덱스는 숫자, 홀수 인덱스는 연산 기호로 나뉨
홀수 인덱스가 어떤 연산 기호인지 확인 후 뒤의 숫자를 연산하는 방식으로 구현

'''

def solution(my_string):
    my_string_list = list(my_string.split())

    answer = int(my_string_list[0])
    for i in range(1, len(my_string_list)-1):
        if i % 2 == 1:
            if my_string_list[i] == '+':
                answer += int(my_string_list[i+1])
            else:
                answer -= int(my_string_list[i+1])
    return answer