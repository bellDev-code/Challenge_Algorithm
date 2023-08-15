# [PGS] 간단한 식 계산하기/04/오슬기

binomial = "43 + 12"

arr = binomial.split()
print(arr)

if arr[1] == '+':
    answer = int(arr[0]) + int(arr[-1])
elif arr[1] == '-':
    answer = int(arr[0]) - int(arr[-1])
else:
    answer = int(arr[0]) * int(arr[-1])