# 두 수의 연산값 비교하기
def solution(a, b):
    # format 함수를 이용하여 해당 정수의 계산식을 문자열로 합침
    # 둘 중 최대값을 리턴값으로 보내기 위해서 max함수를 사용
    return max(int(f"{a}{b}"), int(f"{2 * a * b}"))