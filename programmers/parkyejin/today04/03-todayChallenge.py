# 수박수박수박수박수박수?
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수를 작성하는 문제입니다.

def solution(n):
    answer = ''
    # '수'나 '수박'으로 반복되기 때문에 변수로 설정하고
    one = '수'
    two = '수박'
    if n==1:
        answer = one
    elif n==2:
        answer = two
    elif n > 2 and n <= 10000:
        if n%2==0: # n을 2로 나눈 나머지가 0이면
            answer = two*(n//2) # 2로 나눈 몫을 곱한만큼 출력하고
        else:
            answer = two*(n//2) + one # 아니면 two에 몫을 곱하고 one을 더하여 출력한다. 
    return answer