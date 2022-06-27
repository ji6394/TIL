## Javascript day10
#### 객체
- 배열
- 함수
- 이 외 객체
``` java
const fruits = ['사과','바나나','감','귤']
```
#### 배열.length : 배열 길이
#### 배열[index] : 배열의 해당 요소 출력
#### array.unshift(요소) : 배열 맨 앞에 요소 추가
#### array.push(요소) : 배열 맨 뒤에 요소 추가
#### array.shift() : 배열 맨 앞 요소 삭제
#### array.pop() : 배열 맨 뒤 요소 삭제
#### array.splice(index,크기,추가할 요소) : 삭제, 수정, 추가 모두 가능
#### array.includes(요소) : 해당 요소 포함하는지 여부에 따라 참,거짓 출력
#### array.indexOf(요소) : 해당 요소 index 도출, 없으면 -1
#### array.lastIndexOf(요소) : 해당 요소 index 도출
#### 여러 개 요소 삭제
``` java
const arr = ['가','라','나','라','라','마']
const check = arr.indexOf('라')

while (check>-1){
    arr.splice(check,1)
    check=arr.indexof('라')
}
```
