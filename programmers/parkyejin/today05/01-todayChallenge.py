# 나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수를 작성하는 문제입니다.

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)): 
        if arr[i]%divisor == 0: # 나머지가 0인 경우 
            answer.append(arr[i]) # answer에 추가하고
            answer.sort() # 오름차순 정렬하도록 작성하였고
        else: # 나머지가 0이 아닌 경우
            if i == (len(arr)-1) and len(answer) == 0: # i가 배열에 마지막 원소를 가리키고, answer의 길이가 0으로 값이 없는 경우
                answer.append(-1) # -1을 추가하도록 하였습니다.
    return answer