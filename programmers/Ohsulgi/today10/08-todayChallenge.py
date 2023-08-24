'''
[PGS] 푸드 파이트 대회/08/오슬기

a // b 는 a를 b로 나눈 몫
정방향과 역방향으로 각각 문자열을 만든 뒤
가운데 0과 함께 하나로 합친다

'''

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    answer2 = ''
    for i in range(1, len(food)):
        answer2 += str(i) * (food[i] // 2)
    return answer + '0' + answer2[::-1]