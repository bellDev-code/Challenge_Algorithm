# 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴하는 문제입니다.

def solution(n):
    answer = []
    n_list = list(map(int,str(n))) # list(map(int,str()))로 숫자를 리스트로 변환하였습니다. 
    for i in range(len(n_list)-1,-1,-1): # 리스트의 뒤에서부터 접근하도록 -1 음수 지정하였습니다.
        answer.append(n_list[i])
    return answer