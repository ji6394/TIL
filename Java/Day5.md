## Java 5강
#### 특수문자
- \t : 탭
- \n : 개행
- \' : 작은따옴표
- \" : 큰따옴표
#### 서식문자 : println이 아닌 printf 사용
- %d : 10진수
- %o : 8진수
- %x : 16진수
- %c : 문자
- %s : 문자열
- %f : 실수
#### println은 개행 포함, but printf는 개행 미포함
#### 예시
``` java
int num = 10
System.out.printf("num(8진수)=%o\n",num)
```
#### 서식 문자를 이용해 출력 문자의 정렬과 소수점 제한 가능
``` java
System.out.printf("%5d\n", 123) #우측 정렬
System.out.printf("%.2f\n",0.123456) #소수점 2자리 이하로 제한
```