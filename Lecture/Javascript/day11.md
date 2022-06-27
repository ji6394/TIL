## Javascript 2-25
#### 함수 선언
``` java
function a(parameter){
    console.log(parameter)
}

a('argument')
// argument
```
#### 함수 선언 시 : parameter(매개변수)
#### 함수 호출 시 : argument(인수)
#### console.log(arguments) : arguments는 인수를 배열 형식으로 출력
#### 인수가 매개변수보다 많을 시 초과분 무시하고 함수 호출
#### 화살표 함수
``` java 
const f = (x,y,z) => {
    return x*y*z;
} // {와 return이 이어지면 생략 가능
```
#### 함수 내에서도 변수 선언 가능
#### 객체 리터럴 : 파이썬의 딕셔너리와 비슷
``` java
const zerocho = {
    name : '정지훈',
    age : 25,
    gender : 'm'
}
```
#### 이 때 하위 집합을 속성, 속성의 이름, 속성의 값으로 나누어짐
#### 속성 이름의 경우 따옴표 굳이 필요 없으나 이름에 특수문자나 숫자, 공백이 들어갈 시 따옴표 필요
#### 수정 : zerocho.name = 'hello'
#### 삭제 : delete zerocho.name
#### 메서드 : 객체의 속성 값으로 함수를 넣었을 때
``` java
const debug = {
    log : function(value) {
        console.log(value)
    }
}
```
#### 객체 레퍼런스
- 모양이 같더라도 새로운 각각의 객체 끼리는 다른 값
``` java
{} ===  {} // false
```
``` java
const a = {name : 'zerocho'}
const array = [1,2,a]
console.log(a===array[2]) // true
```
- 객체의 경우 레퍼런스를 활용하여 수정 가능하지만 객체가 아닌 값(문자열, 숫자, 불리언 값) 등은 객체 레퍼런스를 활용하여 수정 불가능. 객체의 경우 해당 객체의 주소를 이용하기에 변경 값이 그대로 적용되지만 객체가 아닌 값의 경우 주소가 아닌 실재 요소 자체를 갖고 있기 때문