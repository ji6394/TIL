## Javascript 3.4
#### document.querySelector('선택자') : 선택자에 해당하는 html 태그 가져오기
#### queryselector로 변수를 선언할 때, 보통 선택자앞에 $표시
#### document.querySelectorAll('선택자') : 해당 선택자 모두 가져오기
#### NodeList : 배열이 아닌 객체
#### 만약 여러 개 있을 때 query selector를 쓰면 맨 앞 요소 가져온다
#### id가 'order'인 span 찾기
``` java
<span id = "word">1</span>
...
<span id = "order"></span>


document.querySelector(#"order") //#은 ID에 해당
```
#### class가 'btn'인 button 찾기
``` java
<button class = "btn">버튼2</button>
<button class = "btn">버튼3</button>

document.querySelector(".btn") //.은 class에 해당
```

``` java
const $span = document.querySelector('div span') //div의 자손인 span 가져오기
```

#### 자식 : 바로 아래 하위단계
#### 자손 : 모든 하위단계
``` java
const $span = document.querySelector('div>span') //div의 자식인 span
```

#### 복잡하면 id 붙이기
#### document.querySelector(선택자 하위선택자 하위선택자)