'''
[PGS] 숫자 찾기/09/오슬기

score의 평균을 구해 avg에 할당
arr.sort() 는 변수에 할당할 수 없지만 sorted(arr)는 변수에 할당 가능
avg를 내림차순으로 정렬 후 rank 할당
rank의 인덱스+1 이 학생들의 등수

'''

def solution(score):
    avg = [sum(i) / 2 for i in score]
    rank = sorted(avg)[::-1]

    answer = [(rank.index(i) + 1) for i in avg]
    return answer