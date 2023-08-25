'''
[PGS] 카드 뭉치/05/오슬기

문자열을 공백으로 나누고 단어별로 2중 리스트로 만든 뒤
각 단어의 0번 인덱스가 알파벳인지 판별하여 알파벳이면 대문자로 만든다
나머지 인덱스는 모두 소문자로 변환한다
'''

def solution(s):
    s_list = [list(i) for i in s.split(' ')]

    answer = []
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j == 0 and s_list[i][j].isalpha() == True:
                s_list[i][j] = s_list[i][j].upper()
            elif j != 0 and s_list[i][j].isalpha() == True:
                s_list[i][j] = s_list[i][j].lower()
        str_ = ''.join(s_list[i])
        answer.append(str_)
    return ' '.join(answer)