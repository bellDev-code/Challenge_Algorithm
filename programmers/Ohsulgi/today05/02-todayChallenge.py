# [PGS] 날짜 비교하기/02/오슬기

def solution(date1, date2):
    if date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] < date2[2]:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0