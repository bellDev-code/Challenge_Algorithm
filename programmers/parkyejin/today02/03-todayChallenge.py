# 두 정수 사이의 합
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수를 작성하는 문제입니다.

def solution(a, b):
    answer = 0

    # a가 b보다 큰 경우에는 두 숫자의 값을 바꾸도록 하였습니다. (아래 for문 돌리기 위해서)
    if a > b: 
        temp = a
        a=b
        b=temp

    # a부터 b까지 더하기 위해 끝값을 b+1로 지정하였습니다.
    for i in range(a,b+1,1):
        answer = answer + i
    return answer