# 카운트 업
def solution(start_num, end_num):
    answer = []
    # start_num 시작하여 end_num에서 +1 해준 이유는 range 함수의 두 번째 인자에 -1이 되어있기 때문
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer