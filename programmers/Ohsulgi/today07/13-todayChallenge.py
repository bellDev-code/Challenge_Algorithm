'''
[PGS] 외계어 사전/13/오슬기

spell의 원소가 dic의 원소에 존재하는지 체크하기 위해 딕셔너리 생성
앞의 원소가 dic의 원소에 존재하지 않으면 뒤 원소는 확인할 필요가 없음

'''

def solution(spell, dic):
    dic_dict = {i:0 for i in dic}

    for i in spell:
        for j in dic:
            if dic_dict[j] == 2:
                pass
            else:
                if i in j:
                    dic_dict[j] = 1
                else:
                    dic_dict[j] = 2

    if 1 in dic_dict.values():
        return 1
    else:
        return 2