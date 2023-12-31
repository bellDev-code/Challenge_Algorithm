---
# 2023 메타버스 아카데미 - 데이터사이언스 알고리즘 스터디 📝
파이썬으로 시작하는 알고리즘

매일 3문제 목표로 파이썬과 친해지기 그리고 하루 1커밋 시작하기

안하면 매우 서운

<br />
<br />

## ✅ git 사용법
1. git 홈페이지 접속 후 다운로드 진행
2. 다운로드 후 cmd 또는 powershell에서 해당 명령어 검색 (git이 설치되어 있는지 확인하는 과정)
```
git -v
ex) git version 2.40.1
```
3. 위의 커맨드가 나온다면 컴퓨터에 git이 다운로드 되었다는 뜻입니다.

## ✅ 시작 방법
1. 밑의 url를 복사한다. (https 형태로 clone)
```
git clone "https://github.com/bellDev-code/Challenge_Algorithm.git"
```
2. 자신의 visual Studio code의 터미널 (ctrl + ~)을 열어 자신이 원하는 디렉토리에 복사한 url을 붙여넣는다.
3. 아무런 에러 메세지가 없을 시, 밑의 명령어를 친다.
```
git pull origin main
```
4. 왜 pull을 먼저하나요?
   - Challenge_Algorithm 레포지토리는 혼자만 사용하는 것이 아닌 스터디분들의 저장소입니다.
   - 스터디원들의 commit의 출동을 예방합니다. (협업 프로젝트 간접 경험 가능)
   - 항상 시작 전 git pull 하는 습관을 들입시다.

<br />
<br />

## ✅ 소스코드 파일 작성 시 이름 규칙
- 최상단은 programmers 폴더 하위에 만들어주세요.
- 폴더 이름은 자신의 영문 이름으로 작성해주세요.
- 자신의 영문이름 폴더 하위에 today01 형식의 폴더 만들어주세요.
```
programmers
 ㄴ leejongho
    ㄴ today01
    ㄴ today02
```
- 위의 형태의 폴더 구조가 생성되어야합니다.
- today01 폴더명 하위에 소스코드 파일 작성
- 문제번호/todayChallenge.py 형태
- ``` 01-todayChallenge.py```
- 위의 소스코드 파일이 한 문제입니다.
- 폴더명 또는 소스코드 파일명에 콜론 ":" 안됩니다 :D

<br />
<br />

## ✅ commit 규칙
- commit 메세지: [문제 출처(플랫폼)]문제이름/ 문제번호 / 한글이름
- description: 문제 주소 (option)
- 터미널에서 명령어 작성법
```
git commit -m "[PGS]문자열출력하기/01/이종호"
```
- 또는 visual studio code 왼쪽 상단의 Source Control에서 commit 할 수 있습니다. 위의 형태로 부탁드립니다.
- 플랫폼 작성법 통일:
  * [PGS] - 프로그래머스
  * [BOJ] - 백준 
  * [ETC] - 그외
- 터미널에서 git push origin main 명령어 사용
- git config Error란? 아마도 처음 진행하시는 분은 config 에러가 발생할 수 있습니다. 
```
git config --list
```
- 위의 명령어를 터미널에서 확인하게 되시면
- user.name과 user.email을 설정해야합니다.
```
git config --global user.name "여러분 닉네임"
```
```
git config --global user.email "여러분 이메일"
```
- 위 명령어를 터미널에 입력하시게 되면 깃허브 홈페이지가 나오고 연결하시면 해결됩니다.
<br />
<br />

## ✅ PR 규칙
- commit 후 challenge_Algorithm의 상단 보시면 pull resquests 눌러줍니다.
- new pull request 생성 버튼 클릭
- PR 제목: 이름 / 문제이름 / 문제번호
- ```leejongho / 문자열 출력하기 / 01 ```
- comment는 자유입니다. 이번주에 풀었던 문제의 알고리즘 분류가 어떻게 되는지, <br> 어떤 문제가 어려웠는지 회고를 작성한다면 개인에게도 도움되고 다른 코드 리뷰어가 참고하기 좋습니다.

<br />
<br />

## ✅ (option)코드리뷰 규칙
- PR에서 코드리뷰를 한다.
- 전체 코드 흐름을 파악한 뒤, 이 분이 어떻게 풀었을까 이해를 한 후 
- 의견제시
  -   잘했다고 생각하는 부분
  -   이렇게 하면 더 좋을 것 같다고 생각하는 부분
  -   왜 이렇게 풀었는지 궁금한 부분
  -   또 다른 풀이 방식 제시
- 코드의 일부분에다 코드리뷰를 해도 되고 전체 코드 밑 or PR 하나 밑에다 코멘트 작성으로 리뷰를 해도 됩니다.

<br />
<br />
