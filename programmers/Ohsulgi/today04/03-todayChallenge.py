# [PGS] 배열의 길이에 따라 다른 연산하기/03/오슬기

def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for j in range(len(arr)):
            if j % 2 == 1:
                answer.append(arr[j] + n)
            else:
                answer.append(arr[j])
    return answer