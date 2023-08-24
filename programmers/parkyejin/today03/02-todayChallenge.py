# 제일 작은 수 제거하기
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수를 작성하는 문제입니다.

def solution(arr):
    answer = []
    if len(arr) == 1: # 배열의 길이가 1인 경우 -1을 리턴하도록 작성하였습니다.
        answer.append(-1)
    else:
        arr.remove(min(arr)) # 그 외인 경우, min() 함수를 사용하여 가장 작은 원소를 제거하도록 하였습니다.
        answer=arr 
    return answer