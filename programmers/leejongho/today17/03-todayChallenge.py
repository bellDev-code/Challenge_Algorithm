# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):    
    stack = []
    # 문자열 s의 처음이 ")" 되면 무조건 false 반환
    if s[0]==")":
        return False

    for el in s:
        # s문자열이 "("이면 만들어 놓은 stack 배열에 넣는다. 
        if el == "(":
            stack.append(el)
        else:
            # stack 배열이 아니면 false 
            if not stack:
                return False
            # 열린 괄호가 없는 상태에서 닫힌 괄호를 만난 경우 false
            # stack에서 최근에 추가된 열린 괄호를 꺼내어 out 변수에 저장
            out = stack.pop()
            # 만약 out이 ")"이면 false
            if out == ")":
                return False
    if stack:
        return False
    else :
        return True