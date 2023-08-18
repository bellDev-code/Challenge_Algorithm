# [PGS] OX퀴즈/15/오슬기

def solution(quiz):
    arr = [list(quiz[i].split()) for i in range(len(quiz))]

    answer = []
    for i in range(len(arr)):
        if arr[i][1] == '+':
            if int(arr[i][0]) + int(arr[i][2]) == int(arr[i][-1]):
                answer.append('O')
            else:
                answer.append('X')
        elif arr[i][1] == '-':
            if int(arr[i][0]) - int(arr[i][2]) == int(arr[i][-1]):
                answer.append('O')
            else:
                answer.append('X')
    return answer