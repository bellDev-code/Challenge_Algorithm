# 나머지가 1이 되는 수 찾기
# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 작성하는 문제입니다.

def solution(n):
    answer = 0
    for i in range(1,n): # 나머지가 1이 되려면 정수 n보다 작으면 되므로 n-1까지
        if n % i == 1: # 나머지가 1이면
            answer = i # answer에 넣고
            break # for문을 나오도록 작성했습니다.
    return answer