# 코드 처리하기
# code = "abc1abc1abc" 
# code[0] = "a", mode=0, ret="a" 

def solution(code):
    # 문자에 따라 mode가 바뀌므로 mode = True를 기본값을 가지는 boolean 형태, ret 문자열을 선언해줍니다.
    mode = True
    ret = ''
    # enumerate함수 사용하여 인덱스와 원소 추출
    for idx, str in enumerate(code):
        # mode가 False, True일 때 if문
        if mode:
            # code[idx] 1이 아니고 idx가 짝수일때, ret 뒤에 str 추가
            if str != '1' and idx % 2 == 0:
                ret = ret + str
                # 모드 변환
            elif str == '1':
                mode = False         
        else:
            # code[idx] 1이 아니고 idx 홀수일때만, ret 뒤에 str 추가
            if str != '1' and idx % 2 != 0:
                ret = ret + str
                # 모드 변환
            elif str == '1':
                mode = True
    # 빈문자열 처리
    if len(ret) == 0:
        return 'EMPTY'
    return ret