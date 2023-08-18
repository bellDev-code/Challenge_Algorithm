# [PGS] 다음에 올 숫자/06/오슬기

def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        a = common[1] - common[0]
        return common[-1] + a
    else:
        b = int(common[1] / common[0])
        return common[-1] * b