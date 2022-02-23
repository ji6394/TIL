## Java 6강
#### 연산자
- 단항 연산자 : 피연산자가 하나 존재
- 이항 연산자 : 피연산자가 2개 존재
- 삼항 연산자...
#### Java에서는 산술 연산 시 해당 피연산자의 자료형에 맞추어서 결과 역시 반환
``` java
int x = 10;
int y = 20;
System.out.println("x/y="+(x/y));

// x/y=0
```
#### 증감 연산자
- ++ : 1 증가
- -- : 1 감소
``` java
int x = 10;
System.out.println("++x="+(++x));
// ++x=11

x = 20;
System.out.prinln("x++="+(x++));
// x++=20
System.out.println(x)
// 21
```
#### 논리 연산자
- && : 전항과 후항이 모두 참일 때 true
- || : 전항과 후항 중 하나라도 참일 때 true
- ! : 해당 항의 상태를 부정
#### 조건 연산자 : 조건식 ? true값 : false값
``` java
int x = 10; int y = 20;
int result = 0;
result = (x>y) ? 1 : 2 ;
System.out.println("result:"+result)
//result:2
```

#### 비트 연산자 : 데이터를 비트단위로 환산하여 연산을 수행하며 다른 연산자보다 연산 속도가 향상
- & : 전항과 후항이 모두 1이면 1
- | : 전항과 후항 중 하나라도 1이면 1
- ^ : 전항과 후항이 다르면 1