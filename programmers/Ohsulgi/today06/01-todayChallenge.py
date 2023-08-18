# [PGS] 정수를 나선형으로 배치하기/01/오슬기

def solution(n):
    answer = [[0] * n for _ in range(n)]

    x, y = 0, 0
    direction = 0

    for i in range(1, (n**2)+1):
        answer[y][x] = i
        if direction == 0:
            if x + 1 == n or answer[y][x+1] != 0:
                direction = (direction + 1) % 4
                y += 1
            else:
                x += 1
        elif direction == 1:
            if y + 1 == n or answer[y+1][x] != 0:
                direction = (direction + 1) % 4
                x -= 1
            else:
                y += 1
        elif direction == 2:
            if x == 0 or answer[y][x-1] != 0:
                direction = (direction + 1) % 4
                y -= 1
            else:
                x -= 1
        elif direction == 3:
            if y == 0 or answer[y-1][x] != 0:
                direction = (direction + 1) % 4
                x += 1
            else:
                y -= 1  
    return answer