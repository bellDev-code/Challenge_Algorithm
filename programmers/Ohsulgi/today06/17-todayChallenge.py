# [PGS] 다항식 더하기/17/오슬기

def solution(polynomial):
    arr = list(polynomial.split())

    cnt = 0
    number = 0
    for i in arr:
        if 'x' in i:
            if len(i) > 1:
                a = i[:-1]
                cnt += int(a)
            else:
                cnt += 1
        elif i == '+':
            pass
        else:
            number += int(i)

    if cnt > 0 and number > 0:
        if cnt == 1:
            return f'x + {number}'
        else:
            return f'{cnt}x + {number}'
    elif cnt > 0 and number == 0:
        if cnt == 1:
            return f'x'
        else:
            return f'{cnt}x'
    elif cnt == 0 and number > 0:
        return f'{number}'
    else:
        return '0'