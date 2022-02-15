## Java 2강
#### 환경변수 세팅 : 컴퓨터 내 어느 디렉토리에서나 Java 실행할 수 있도록 세팅해주어야 함
#### 시스템 설정 , 환경 변수, Jdk파일 입력한 후 path에도 jdk폴더의 bin 폴더 path 추가
#### 명령프로토콜에서 java -version 혹은 javac-version으로 확인 가능
#### java 구동 원리
1. java 소스(xxx.java)
2. java 컴파일러(javac.exe) : 소스코드를 기계어로 바꿈
3. 바이트 코드 파일(xxx.class)
4. JVM 구동(java.exe)
5. Link(기계어, 실행) : 메모리 로딩, 실행 준비, 실행 결정, 초기화
#### 메모장으로 java 소스 생성 후 명령 프로토콜에서 해당 디렉토리 이동(cd c;...), javac.exe xxx.java 와 java xxx 의 과정을 거쳐 실행 가능
#### 하지만 eclipse는 이 모든 컴파일, 디버깅, 실행 과정을 한 번에 다 해줌!
#### <mark>메모장 직접 입력하여 java 실행할 때 파일명과 클래스 명은 완전히 일치해야 함</mark>
- C 계열 : 직접 메모리 관리, 메모리 누수나 타 프로그램 작동 오류 가능성
- java 계열 : 메모리 접근 불가능, GC(garbage collector)가 메모리 회수.