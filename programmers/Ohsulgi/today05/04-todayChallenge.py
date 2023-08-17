# [PGS] 그림 확대/04/오슬기

def solution(picture, k):
    answer = []
    for i in picture:
        arr = list(i)
        arr2 = []
        for j in arr:
            arr2.append(j * k)
        result = ''.join(arr2)
        for _ in range(k):
            answer.append(result)
    return answer