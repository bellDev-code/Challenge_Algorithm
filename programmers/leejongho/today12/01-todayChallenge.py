# 첫 번쨰로 나오는 음수
# 파이썬 enummerate 함수를 이용하여 인덱스와 값을 가져옴
def solution(num_list):
    for idx, num in enumerate(num_list):
        # 음수일 때 해당되는 익덱스를 리턴
        if num < 0:
            return idx
    return -1