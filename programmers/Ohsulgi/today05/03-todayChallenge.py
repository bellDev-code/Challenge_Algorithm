# [PGS] 커피 심부름/03/오슬기

def solution(order):
    answer = 0
    for i in order:
        if 'ame' in i:
            answer += 4500
        elif 'cafe' in i:
            answer += 5000
        elif i == 'anything':
            answer += 4500
    return answer