#문자열 섞기
def solution(str1, str2):
    result = ""
    length = min(len(str1), len(str2))

    for i in range(length):
        result += str1[i] + str2[i] 
    
    if len(str1) > length:
        result += str1[length:]
    elif len(str2) > length:
        result += str2[length:]

    return result

str1 = "aaaaa"
str2 = "bbbbb"
print(solution(str1, str2))