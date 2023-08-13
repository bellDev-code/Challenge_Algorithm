# [PGS] 홀수 vs 짝수/03/오슬기

def solution(num_list):
    num_list.insert(0, 0)
    
    sum1, sum2 = 0, 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum1 += num_list[i]
        else:
            sum2 += num_list[i]
            
    return max(sum1, sum2)