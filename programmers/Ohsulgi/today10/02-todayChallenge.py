'''
[PGS] 숫자 문자열과 영단어/02/오슬기

문자열을 변환하고자 하는 숫자와 key : value 로 매치하여 딕셔너리로 만들고
주어진 문자열에 해당하는 문자열이 있으면 숫자로 치환한다

'''

def solution(s):
    num_dict = {
        'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
        'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
    }

    for i in num_dict.keys():
        if i in s:
            s = s.replace(i, str(num_dict[i]))
    return int(s)