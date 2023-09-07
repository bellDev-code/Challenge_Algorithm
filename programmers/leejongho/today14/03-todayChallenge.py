# 배열에서 문자열 대소문자 변경하기

# strArr = ["AAA","BBB","CCC","DDD"]
# result = ["aaa","BBB","ccc","DDD"]

# enumerate 함수로 인덱스에 따른 값 구하고 인덱스가 홀수 짝수인지 구별하고
# 짝수면 lower 함수, 홀수면 upper 함수로 새로운 배열에 넣어준다. 
def solution(strArr):
    result = []
    for idx, el in enumerate(strArr):
        if idx % 2 == 0:
            result.append(el.lower())
        else:
            result.append(el.upper())
    return result