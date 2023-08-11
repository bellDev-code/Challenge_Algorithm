# 대소문자 바꿔서 출력하기
str = input()
a = ''

# for문 활용하여 문자열 원소 체크
for s in str:
    # if문 활용하여 소문자 대문자 체크
    if(s.isupper()):
        a = a + s.lower()
    else:
        a = a + s.upper()
print(a)