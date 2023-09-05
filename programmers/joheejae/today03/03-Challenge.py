#문자열잘라서정렬
#1
def solution(myString):
    substrings = myString.split("x")
    result = sorted([substring for substring in substrings if substring])
    return result

#2
def solution(myString):
    return sorted(string for string in myString.split('x') if string)
