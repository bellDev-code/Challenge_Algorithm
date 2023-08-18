# [PGS] 정사각형으로 만들기/03/오슬기

def solution(arr):
    x = len(arr[0])
    y = len(arr)

    if x == y:
        return arr
    elif x < y:
        for _ in range(y-x):    
            for i in range(len(arr)):
                arr[i].append(0)
    elif x > y:
        for _ in range(x-y):
            arr.append([0] * len(arr[0]))
    
    return arr