## 선형대수학 1강
#### linear equation : 일차방정식
#### system of linear equation : 일차방정식 집합
#### consistent/ inconsistent : 해 존재/ 해가 존재하지 않음
#### elementary row operations
+ replacement : 특정 행의 곱을 다른 행에 더하기
+ scaling : 특정 행을 곱하기
+ interchange : 특정 행 간 순서 바꾸기
#### equivalent : linear equation 들이 같은 해를 가질 때
#### row equivalent : elementary row operations를 거친 row들, 역시 같은 해를 가짐
- - -
## Java 입문 1강
#### 소스(개발자 업무 영역) → 컴파일러 → 작업물
#### Java는 C++에서 발전한 언어
- 객체지향언어
- JRE를 활용하여 운영체제가 자유롭다
- 웹 및 모바일 프로그래밍이 쉬움
- GC(Garbage collector)를 통한 메모리 자동 관리 가능
- 실행속도 개선됨
#### Java 프로그램 구성
- JDK : Java Developer kit(개발자용 도구)
- JRE : Java 프로그램이 실행될 수 있는 환경
- API : JVM을 컨트롤하는 기능
- JVM : Java virtual machine, 핵심
#### Oracle을 통해 Java 다운, IDE로는 Eclipse 다운
#### Java file 만들기, 파일을 만들게되면 해당 폴더에 src 폴더와 bin 폴더 생성
- src : 실제 만들어낸 코드 내장
- bin : binary, 컴파일 후 컴퓨터가 이해할 수 있는 파일
#### Class : Java 프로그램을 구성하는 파일
#### Java 편집창에서 New java file 만들기. 이후 src 우클릭 후 new 에서 Class 생성
#### main method는 많은 class 파일들 중 가장 먼저 실행할 파일 설정하는 메서드
#### main method 만들기 : 'main'입력 후 ctrl+space, main method 클릭
#### Hello world 출력하기 : 콘솔 창에서 sysout 입력 후 assist 실행. 괄호 안에 <mark>쌍따옴표("")</mark>사용하여 내용 출력
#### 이후 반드시 <mark>저장</mark> 하여 해당 클래스 파일 컴파일
#### 실행의 경우 해당 전체 폴더 우클릭 후 Run, Java file 누르면 아래에 실행됨
- - -
## Javascript 입문 1강
#### chrome에서 새 탭 , F12 누른 후 console
#### () : parantheses, 소괄호 / {} : braces, 중괄호 / [] : brackets, 대괄호
#### REPL : 브라우저의 콘솔은 입력받고(Read), 입력받은 명령을 평가하고(Evaluate), 해당 명령을 출력한 후(Print), 새로운 입력을 기다린다(Loop).
#### 위 내용과 같은 입력 : 방향키 위 혹은 아래
#### 순서도 기호
- 두 겹의 원 : 시작 혹은 끝
- 타원 : 일반 절차
- 마름모 : 판단 절차 (예/아니오, 다지선다)
- 두 겹의 사각형 : 특수한 상황(대기, 이벤트 발생)
- 화살표 : 절차
#### Hello world 출력하기 : console.log('Hello world!')

- - -
## 데이터분석 Chapter 10: 데이터 집계와 그룹 연산
#### groupby
``` python
df['data1'].groupby(df['key1']).mean()
df['data1'].groupby([df['key1'],df['key2']])
```
#### groupby 이터레이션(이름,묶음)
``` python
for name, group in df.groupby('key1'):
    print(name)
    print(group)
```
#### groupby는 딕셔너리, Series, 함수로 그룹핑 가능
#### multiindex로 열을 구성하였을 경우 level 예약어를 사용