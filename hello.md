### Git 사용법
1. git 초기 설정
    - git config --global user.name "(이름)"
    - git config --global user.email "(이메일)"
2. git init : 폴더를 git에 맡기기
3. .gitignore : git에 맡기지 않을 파일 추가
4. git 추가
    - git add "파일이름" : 일부 추가
    - git add -A or . : 전체 추가
5. git commit 하기
    - git commit -m "commit 이름"
    - git commit -am "commit 이름" : add 와 commit을 한번에 수행
6. 시간 되돌리기 : Reset vs Revert
    - Reset : 미래를 삭제하고 과거로 되돌아가기
        - git reset --hard log번호
    - Revert : 미래 남기고 과거로 되돌아가기
        - git revert log번호
7. j와 k로 스크롤 조정 가능