# [PGS] 1로 만들기/10/오슬기

def solution(num_list):
    arr = [1 for i in range(len(num_list))]
    cnt = 0
    i = 0
    while True:
        if arr == num_list:
            return cnt

        if num_list[i] != 1:
            if num_list[i] % 2 == 0:
                num_list[i] = int(num_list[i] / 2)
                cnt += 1
            else:
                num_list[i] = int((num_list[i] - 1) / 2)
                cnt += 1
        else:
            i += 1