'''
[PGS] 직사각형 넓이 구하기/12/오슬기

모든 변이 축과 평행하므로 x, y의 차이를 구하면 된다
abs() : 절대값 함수

'''

def solution(dots):
    dots.sort()
    y = abs(dots[0][1] - dots[1][1])
    x = abs(dots[0][0] - dots[2][0])
    
    return x * y