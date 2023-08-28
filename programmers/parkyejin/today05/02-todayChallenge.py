# 문자열 내림차순으로 배치하기
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수를 작성하는 문제입니다.

def solution(s):
    answer = ''
    answer = "".join(sorted(s, reverse=True)) # sorted() 함수를 활용하여 정렬하였는데, 리스트 형태로 반환하기 때문에 join()을 사용하여 문자열로 합쳤습니다.
    return answer