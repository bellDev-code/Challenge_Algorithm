'''
[PGS] 배열 회전시키기/08/오슬기

insert(삽입할 인덱스, 삽입할 요소)
pop()은 가장 뒤 인덱스의 요소를 삭제하지만
pop(0)는 0번 인덱스의 요소를 삭제하고 나머지 인덱스의 요소들을
앞으로 이동시킨다

'''

def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers[-1])
        numbers.pop()
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
    return numbers

