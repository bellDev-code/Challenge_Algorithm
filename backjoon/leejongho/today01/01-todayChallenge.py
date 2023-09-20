# 백준 2588번 곱셈

# 입력값
# 472
# 385

# 출력값
# 2360
# 3776
# 1416
# 181720

A = int(input()) # 정수로 변경
B = input() # 문자열 그대로

first = A * int(B[2])
second = A * int(B[1])
third = A * int(B[0])
final = A * int(B)

print(first, second, third, final, sep='\n')