# 서울에서 김서방 찾기
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수를 작성하는 문제입니다.

def solution(seoul):
    answer = '' 
    kim = 0  # Kim의 인덱스값을 저장할 변수를 설정하였습니다.
    if len(seoul) >= 1 and len(seoul) <= 1000: # seoul은 길이 1 이상, 1000 이하인 배열이기에 조건을 추가하고
        for i in range(len(seoul)): 
            if seoul[i] == 'Kim': 
                kim = i # Kim을 찾으면 해당 인덱스값(i)를 kim 변수에 넣고
    answer = '김서방은 '+str(kim)+'에 있다' # 정수형인 kim 변수를 문자열로 변환하여 출력하였습니다.
    return answer 