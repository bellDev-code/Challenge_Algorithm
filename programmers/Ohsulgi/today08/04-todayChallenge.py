'''
[PGS] 공 던지기/04/오슬기

한 명을 건너 뛰기 때문에 i가 짝수 일 때에만 값을 저장
numbers[0]를 numbers의 맨 뒤에 추가하고 pop(0)를 통해
0번 인덱스를 삭제하는 것으로 순환구조 구현

'''

def solution(numbers, k):
    i = 0
    answer = 0
    while True:
        if k == 0:
            break

        if i % 2 == 0:
            answer = numbers[0]
            i += 1
            k -= 1
        else:
            i += 1

        numbers.append(numbers[0])
        numbers.pop(0)
    return answer