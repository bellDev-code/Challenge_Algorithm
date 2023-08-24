# 가운데 글자 가져오기
# 단어 s의 가운데 글자를 반환하는 함수를 작성하는 문제입니다.

def solution(s):
    answer = ''
    # 단어의 길이가 짝수/홀수인 경우를 나누어
    # 길이를 반으로 나눈 값을 활용하여 글자를 반환하도록 작성하였습니다.
    if len(s)%2 == 0: 
        answer = s[len(s)//2-1] + s[len(s)//2] 
    else:
        answer = s[len(s)//2]
    return answer