# 문자열 다루기 기본
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수를 구현하는 문제입니다.

def solution(s):
    answer = True
    if len(s)==4 or len(s)==6: # 문자열의 길이를 먼저 확인하고
        answer = s.isdigit() # isdigit() 함수를 사용하여 숫자인지 아닌지 확인하였습니다.
    else:
        answer = False 
    return answer