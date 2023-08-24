# 이어 붙인 수
def solution(num_list):
    # 빈 배열
    odd_list = []
    even_list = []
    
    # 홀 짝 구분
    for i in num_list:
        if i % 2 == 0:
            even_list.append(str(i))
        else:
            odd_list.append(str(i))
    
    # 홀수 문자열로 넣어둔 원소를 다시 정수로
    odd_num = int(''.join(odd_list))
    even_num = int(''.join(even_list))
    
    total = odd_num + even_num
    
    return total