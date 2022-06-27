## Java 4강
### 기본자료형
#### 자료형은 기본 자료형과 객체 자료형으로 나누어진다.
#### 기본 자료형 : 데이터가 변수에 직접 저장
#### 객체 자료형 : 객체 메모리 주소가 변수에 저장
#### 기본자료형
- 정수형
    - byte : 256범위의 숫자 표현, 1byte
    - char : 'a'나 'b'와 같은 문자 표현, 아스키코드 이용, 2byte
    - short : 숫자, 2byte
    - int : 4byte
    - long : 8byte
- 실수형
    - float : 4byte
    - double : 8byte
- 논리형
    - boolean : 1byte
#### 예시
``` java
public class Mainclass {

    public static void main(String[] args) {
        char c = 'a';
        System.out.printIn("c="+c);
        int b = 10;
        System.out.printIn("b="+b);
        double d = 10.258;
        System.out.printIn("d="+d);
        boolean e = false;
        System.out.printIn("e="+e);
        String s = "Hello Java World!";
        System.out.printIn('s='+s);
    }
}
```
#### 묵시적 형 변환 vs 명시적 형 변환
#### 묵시적(자동적) 형 변환 : 작은 공간에서 큰 공간으로
``` java
byte b = 10;
int i = b;
System.out.printIn("i="+i);
```
#### 명시적 형 변환 : 큰 공간에서 작은 공간으로, 명시적으로 해당 기본형 입력 필요
``` java
int i = 12;
byte b = (byte)i;
```
#### 만약 명시적 형 변화 시 데이터의 함량을 초과하는 경우 데이터가 누실될 수 있음
``` java
i = 123456;
byte bin = (byte)i; #데이터 누실*
```
