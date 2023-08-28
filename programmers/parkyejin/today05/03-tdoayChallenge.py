# 정수 내림차순으로 배치하기
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴하는 함수를 작성하는 문제입니다.

def solution(n):
    answer = 0
    answer_str = "".join(sorted(str(n), reverse=True)) # 정수를 문자열로 변환하여 sorted() 함수를 활용하여 정렬하고, 리스트로 반환하기 때문에 join()을 사용하여 문자열로 반환하도록 하였습니다.
    answer = int(answer_str) # 문자열은 다시 정수로 변환하였습니다.
    return answer
