'''
[PGS] 컨트롤 제트/06/오슬기

문자열을 리스트로 변환하여 숫자가 나오면 더하고
z가 나오면 그 전 인덱스를 뺀다

'''

def solution(s):
    s_list = list(s.split())

    answer = 0
    for i in range(len(s_list)):
        if s_list[i] != 'Z':
            answer += int(s_list[i])
        else:
            answer -= int(s_list[i-1])
    return answer