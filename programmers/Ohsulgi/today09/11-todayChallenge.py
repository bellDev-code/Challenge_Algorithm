'''
[PGS] 이상한 문자 만들기/11/오슬기

문자의 앞, 뒤에도 공백이 올 수 있으니 .split(' ')을 해주어야 리스트에 공백도 추가된다
단어별로 for문을 돌려 짝수 인덱스는 대문자로 만들고 홀수 인덱스는 소문자로 만들어준다

'''

def solution(s):
    s_list = list(s.split(' '))

    answer = []
    for j in s_list:
        arr = ''
        for k in range(len(j)):
            if k % 2 == 0:
                arr += j[k].upper()
            else:
                arr += j[k].lower()
        answer.append(arr)
    return ' '.join(answer)