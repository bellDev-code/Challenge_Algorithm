'''
[PGS] 시저 암호/01/오슬기

알파벳 대문자 리스트와 소문자 리스트를 각각 만들고
주어지는 문자열의 i번째 인덱스가 리스트에 속하면 (원래 문자열 + n) % 26를 인덱스로 하여 순환구조로 출력하게 한다
리스트에 속하지 않은 문자열은 공백을 출력하도록 한다

'''

def solution(s, n):
    arr2 = [chr(i) for i in range(65,91)]
    arr3 = [chr(i) for i in range(97,123)]

    answer = ''
    for i in s:
        if i in arr2:
            if i == 'Z':
                answer += arr2[-1 + n]
            else:
                answer += arr2[(arr2.index(i) + n) % 26]
        elif i in arr3:
            if i == 'Z':
                answer += arr3[-1 + n]
            else:
                answer += arr3[(arr3.index(i) + n) % 26]
        else:
            answer += ' '
    return answer
