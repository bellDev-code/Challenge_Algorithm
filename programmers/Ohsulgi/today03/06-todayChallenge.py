# [PGS] rny_string/06/오슬기

def solution(rny_string):
    string = ['rn' if i == 'm' else i for i in rny_string]
    answer = ''.join(string)
    return answer