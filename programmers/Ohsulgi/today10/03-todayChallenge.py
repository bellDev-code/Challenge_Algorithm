'''
[PGS] [1차] 비밀지도/03/오슬기

arr1과 arr2의 숫자를 bin() 함수를 사용해 2진수로 바꿨을 때 0번 인덱스가 "0" 이면
생략이 되어 자리수가 안맞기 때문에 str.zfill() 메서드로 n자리를 맞춰준다

같은 인덱스에 해당하는 2진수 중 어느 한쪽이라도 1이 포함되어있으면 1로 할당한다

'''

def solution(n, arr1, arr2):
    base = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(arr1)):
        binary1 = str(bin(arr1[i])[2:]).zfill(n)
        binary2 = str(bin(arr2[i])[2:]).zfill(n)

        for j in range(len(binary1)):
            if binary1[j] == '1' or binary2[j] == '1':
                base[i][j] = 1

    answer = []
    for k in base:
        base_string = ''
        for l in k:
            if l == 1:
                base_string += '#'
            else:
                base_string += ' '
        answer.append(base_string)
    return answer