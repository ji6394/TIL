## Javascript 8일차
#### 조건부 연산자 : 조건식 ? 참 : 거짓 ;
#### Javascript는 스페이스바 민감함, 주의하자
``` java
let value = 5 > 0 ? '참입니다' : '거짓입니다';
```
#### 조건부연산은 중첩하여 사용 가능. 헷갈릴 때는 괄호로 우선순위 정해주자
``` java
let condition1 ? conditon2 ? '둘다 참입니다' : 'codnition1만 참' : '둘 다 거짓입니다';
```
#### default는 default : 로 사용, switch에서 case를 사용할 때는 여러개 사용 가능
#### 반복문 while
``` java
while (조건식){
    동작문;
}
```
#### i++ == i += 1
#### 반복문 for : for (시작,조건,종료){동작문;}
#### for의 시작,조건,종료는 생략 가능