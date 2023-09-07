# 배열 만들기
def solution(n, k):
    # range 함수의 첫번째 매개변수(start : 해당 정수부터 시작), 두 번째 매개변수(stop - 1: 해당 범위까지 -1되어 있는점 주의)
    # 세 번째 매개변수(step : 해당 정수만큼 늘어난다.)
    arr = range(k, n+1, k)
    return list(arr)