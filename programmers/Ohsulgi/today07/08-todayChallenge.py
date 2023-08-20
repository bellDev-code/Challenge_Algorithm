'''
[PGS] 숫자 찾기/08/오슬기

정수 n을 answer 배열로 만든 뒤 k가 있는 인덱스를 출력
인덱스는 0부터 시작하므로 +1

'''

def solution(num, k):
    answer = [int(i) for i in str(num)]
    if k in answer:
        return answer.index(k) + 1
    else:
        return -1