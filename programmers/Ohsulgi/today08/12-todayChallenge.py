'''
[PGS] 가까운 수/12/오슬기

array를 오름차순으로 정렬한 후 n과의 차이를 distance에 할당
distance의 가장 작은 값의 인덱스에 해당하는 값을 array에서 찾아서 출력

'''

def solution(array, n):
    array.sort()
    distance = [abs(n-i) for i in array]
    return array[distance.index(min(distance))]