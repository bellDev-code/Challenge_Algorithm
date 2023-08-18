# [PGS] 옹알이 (1)/05/오슬기

def solution(babbling):
    arr = ["aya", "ye", "woo", "ma", '']
    result = [a+b+c+d+e for a in arr for b in arr for c in arr for d in arr for e in arr]

    answer = 0
    for i in babbling:
        if i in result:
            answer += 1
    return answer