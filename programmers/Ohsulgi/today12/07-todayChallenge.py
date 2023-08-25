'''
[PGS] 올바른 괄호/07/오슬기

stack 구조는 입력한 순서대로 배열로 쌓고 나중에 입력된 원소가 먼저 출력이 된다
이를 이용해 "(" 일 경우에는 스택에 추가하고 ")" 일 경우 스택에서 맨 뒤 원소를 제거한다
마지막으로 스택에 원소가 남아있으면 짝지어져있지 않다는 뜻이므로 False를 출력한다

'''

def solution(s):
    s_list = list(s)

    stack = []
    for i in range(len(s_list)):
        if len(stack) == 0 or s_list[i] == '(':
            stack.append(s_list[i])
        elif s_list[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s_list[i])

    if len(stack) == 0:
        return True
    else:
        return False