# 하샤드 수
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수를 완성하는 문제입니다.

def solution(x):
    answer = True
    sum=0
    x_list=list(map(int,str(x))) # 각 자릿수를 더하기 위해 숫자를 리스트로 변환하였습니다.
    for i in range(len(x_list)):
        sum=sum+x_list[i] # 각 자릿수를 더하는 sum 변수를 생성하고
    if x%sum == 0: # 나머지를 계산하여 하샤드 수인지 판단하도록 조건문을 돌렸습니다.
        answer
    else:
        answer=False
    return answer