'''
[PGS] 로그인 성공?/10/오슬기

아이디를 체크한 후 패스워드를 체크하므로
아이디를 먼저 조건문으로 검사 후 통과 하면 패스워드 검사
for문을 모두 지날때까지 해당되는 아이디가 없으면 fail 반환

'''

def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'