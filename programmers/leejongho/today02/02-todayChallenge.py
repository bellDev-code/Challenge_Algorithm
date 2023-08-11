# 홀짝 구분하기
a = int(input())

# if문을 통해서 a를 2로 나누어 홀짝 구분함 
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")