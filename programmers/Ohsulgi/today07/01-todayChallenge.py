'''
[PGS] 7의 개수/01/오슬기

int형 변수는 슬라이싱이 불가능 하므로
str로 바꿔서 7의 개수를 카운트한 뒤 answer로 반환

'''


def solution(array):
    answer = 0
    for i in array:
        if '7' in str(i):
            answer += str(i).count('7')
    return answer