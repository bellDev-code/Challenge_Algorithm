'''
[PGS] K번째수/05/오슬기

commands의 0번 인덱스부터 1번 인덱스까지 슬라이싱 한 후
정렬하여 2번 인덱스에 해당하는 값을 리스트에 추가한다

'''

def solution(array, commands):
    answer = []
    for i in commands:
        sliced_array = array[i[0]-1 : i[1]]
        sliced_array.sort()
        answer.append(sliced_array[i[2]-1])
    return answer