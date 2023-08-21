# 더 크게 합치기
def solution(a, b):
    # 양의 정수 a, b를 문자열로 합치면
    # 9 91 => 991 다시 int로 변경
    res = int(str(a) + str(b))
    res2 = int(str(b) + str(a))
    
    # 두 정수를 max 함수로 최대값을 찾는다.
    return max(res, res2)