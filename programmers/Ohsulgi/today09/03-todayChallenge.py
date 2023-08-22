'''
[PGS] 합성수 찾기/03/오슬기

while문으로 n의 값을 하나씩 줄이면서 n의 약수를 divisor에 할당
divisor의 길이가 3 이상이면 answer의 값에 1 추가

'''

def solution(n):
    answer = 0
    while n > 0:
        divisor = [i for i in range(1, n+1) if n % i == 0]
        if len(divisor) >= 3:
            answer += 1
        n -= 1
    return answer