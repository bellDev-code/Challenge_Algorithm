'''
[PGS] 영어가 싫어요/03/오슬기

0부터 9까지 담은 arr을 만든 뒤 문자열과 그 숫자에 해당하는
arr의 인덱스를 치환

'''

def solution(numbers):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(arr)):
        numbers = numbers.replace(arr[i], str(arr.index(arr[i])))
    return int(numbers)