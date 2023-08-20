'''
[PGS] 자릿수 더하기/06/오슬기

정수를 str로 바궈 슬라이싱 한 후 int로 다시 바꿔 리스트에 추가

'''

def solution(n):
    answer = [int(i) for i in str(n)]
    return sum(answer)