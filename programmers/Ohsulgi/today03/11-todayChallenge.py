# [PGS] 무작위로 K개의 수 뽑기/11/오슬기

def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break

    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    return answer