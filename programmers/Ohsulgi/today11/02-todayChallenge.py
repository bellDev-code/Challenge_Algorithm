'''
[PGS] 추억 점수/02/오슬기

이름과 포인트를 매칭시키는 딕셔너리를 생성
for문을 돌면서 딕셔너리에서 이름으로 포인트를 찾아서 합계

'''

def solution(name, yearning, photo):
    yearning_dict = {name[i] : yearning[i] for i in range(len(name))}

    answer = [sum([yearning_dict[j] if j in yearning_dict else 0 for j in i]) for i in photo]
    return answer
