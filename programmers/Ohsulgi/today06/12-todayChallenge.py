# [PGS] 겹치는 선분의 길이/12/오슬기

def solution(lines):
    arr1 = [i for i in range(lines[0][0], lines[0][1])]
    arr2 = [i for i in range(lines[1][0], lines[1][1])]
    arr3 = [i for i in range(lines[2][0], lines[2][1])]

    answer = 0
    for n in range(-100, 101):
        if (n in arr1 and n in arr2) or (n in arr3 and n in arr2) or (n in arr1 and n in arr3) or (n in arr1 and n in arr2 and n in arr3):
            answer += 1
    
    return answer