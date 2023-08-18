# [PGS] 문자열 밀기/09/오슬기

def solution(a, b):
    a_ = list(a)
    b_ = list(b)

    cnt = 0
    for _ in range(len(a_)):
        if a_ == b_:
            return cnt

        a_.insert(0, a_[-1])
        a_.pop()
        cnt += 1
    return -1
