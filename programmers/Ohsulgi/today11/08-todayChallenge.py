'''
[PGS] 모의고사/08/오슬기

각각 리스트의 길이가 다르므로 n_idx를 지정해서 순환구조를 만든다
정답을 맞춘 사람의 인덱스에 점수를 추가한 뒤 최고점을 맞은 사람을 출력해 오름차순으로 정렬한다

'''

def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    for i in range(len(answers)):
        s1_idx = i % 5
        s2_idx = i % 8
        s3_idx = i % 10

        if answers[i] == s1[s1_idx]:
            score[0] += 1
        if answers[i] == s2[s2_idx]:
            score[1] += 1
        if answers[i] == s3[s3_idx]:
            score[2] += 1

    answer = [i+1 for i in range(len(score)) if score[i] == max(score)]
    answer.sort()
    return answer