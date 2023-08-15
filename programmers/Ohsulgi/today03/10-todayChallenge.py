# [PGS] 배열 만들기 6/10/오슬기

def solution(arr):
    i = 0
    stk = []
    while len(arr) > i:
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif len(stk) > 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1

    if len(stk) > 0:
        return stk
    else:
        return [-1]