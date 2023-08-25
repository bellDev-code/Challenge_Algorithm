#마지막 두 원소
def solution(num_list):
    # 배열에서 음수는 마지막부터 가져옵니다.
    # 즉 -1 마지막 그다음 -2를 통해 if문을 생각하여 새로운 배열을 append 합니다.
    if num_list[-1] > num_list[-2]:
        num = num_list[-1] - num_list[-2]
        num_list.append(num)
    else:
        num_list.append(num_list[-1] * 2)
    return num_list