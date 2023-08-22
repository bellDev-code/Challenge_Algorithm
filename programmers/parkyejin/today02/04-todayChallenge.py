# x만큼 간격이 있는 n개의 숫자
# 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴하는 문제입니다.

def solution(x, n):
    answer = []
    if x!=0: # x가 0이 아닌 경우
        for i in range(x,x*(n+1),x): # 입력값 x부터 x*(n+1)-1 까지 x씩 증가하는 값을 리스트에 추가하도록 for문 작성하였습니다.
            answer.append(i)
    else: # x가 0인 경우에는 
        for i in range(n): # n만큼 0을 출력하도록 작성하였습니다.
            answer.append(0)
    return answer

# x가 0인 경우를 고려하지 않을 경우 런타임 에러가 발생하였습니다.