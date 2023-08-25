'''
[PGS] 실패율/02/오슬기

각각의 스테이지와 실패율을 나타내는 딕셔너리를 생성한다
i번 스테이지의 실패율을 구한 뒤 stages에서 i원소를 모두 삭제한다
딕셔너리를 value를 기준으로 내림차순으로 정렬한 뒤 key값만 리스트로 출력한다

'''

def solution(N, stages):
    stages.sort()
    fail_late = {i : 0 for i in range(1, N+1)}
    for i in range(1, N+1):
        if len(stages) > 0:
            fail_late[i] = stages.count(i) / len(stages)
            while i in stages:
                stages.remove(i)
        else:
            fail_late[i] = 0

    answer = sorted(fail_late.items(), key=lambda x : x[1], reverse=True)
    answer = [answer[i][0] for i in range(len(fail_late))]
    return answer