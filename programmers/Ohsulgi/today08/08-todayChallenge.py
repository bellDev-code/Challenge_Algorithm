'''
[PGS] 한 번만 등장한 문자/08/오슬기

문자열의 각 원소를 key로 하는 딕셔너리를 생성하여 반복문을 돌면서 등장한 횟수를 value로 저장
value가 1인 key만 리스트로 추출하여 사전 순으로 정렬

'''

def solution(s):
    s_dict = {}
    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i] += 1

    s_list = [i for i in s_dict if s_dict[i] == 1]
    s_list.sort()

    answer = ''.join(s_list)
    return answer