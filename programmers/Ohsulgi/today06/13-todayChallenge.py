# [PGS] 안전지대/13/오슬기

def solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for m in range(max(i-1, 0), min(i+2, len(board))):
                    for n in range(max(j-1, 0), min(j+2, len(board))):
                        if board[m][n] == 0:
                            board[m][n] = 2

    answer = 0
    for k in range(len(board)):
        answer += board[k].count(0)
    return answer