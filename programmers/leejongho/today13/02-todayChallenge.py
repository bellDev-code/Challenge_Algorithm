# 5명씩
def solution(names):
    newArr = []
    # enumerate 함수로 인덱스 값 구함
    for idx, el in enumerate(names):
        # 인덱스 5로 나누어 떨어지는 조건식으로 새로운 배열에 append
        if idx % 5 == 0:
            newArr.append(el)
    return newArr