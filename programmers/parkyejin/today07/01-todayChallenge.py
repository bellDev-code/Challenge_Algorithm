# 문자열 내 p와 y의 개수
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 함수를 완성하는 문제입니다.

def solution(s):
    answer = True

    # 문자열 내 특정 문자의 갯수를 세는 count() 함수를 사용하였습니다.
    p_sum = s.count('p') + s.count('P')
    y_sum = s.count('y') + s.count('Y')
    
    if p_sum == y_sum:
        answer = True
    else:
        answer = False
        
    return answer