'''
[PGS] 캐릭터의 좌표/11/오슬기

board를 0을 기준으로 x,y의 최대값으로 분리
keyinput의 원소대로 이동하는 함수 구현
최대값에 도달하더라도 반대 방향으로는 움직일 수 있음을 주의

'''

def solution(keyinput, board):
    max_x = [-1 * int((board[0] - 1) / 2), int((board[0] - 1) / 2)]
    max_y = [-1 * int((board[1] - 1) / 2), int((board[1] - 1) / 2)]

    answer = [0, 0]
    for i in keyinput:
        if i == 'up':
            if max_y[0] <= answer[1] < max_y[1]:
                answer[1] += 1
        elif i == 'down':
            if max_y[0] < answer[1] <= max_y[1]:
                answer[1] -= 1
        elif i == 'right':
            if max_x[0] <= answer[0] < max_x[1]:
                answer[0] += 1
        else:
            if max_x[0] < answer[0] <= max_x[1]:
                answer[0] -= 1
    return answer