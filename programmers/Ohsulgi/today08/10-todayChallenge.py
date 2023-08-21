'''
[PGS] 숨어있는 숫자의 덧셈 (2)/10/오슬기

re.sub() 메서드와 정규표현식을 이용하여 숫자가 아닌 문자열을 모두 띄어쓰기를 포함한 공백으로 변환
띄어쓰기를 포함하지 않으면 연속된 숫자도 모두 1개 단위로 쪼개지기 때문

'''

def solution(my_string):
    import re
    arr = re.sub('[^0-9]',' ',my_string).split(' ')

    answer = 0
    for i in arr:
        if i != '':
            answer += int(i)
    return answer