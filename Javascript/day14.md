## Javascript 끝말잇기(첫번째 사람 입력)
``` java
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>끝말잇기</title>
</head>
<body>
 <div><span id = 'order'>1</span>번째 참가자</div>
 <div>제시어: <span id = 'word'></span></div>
 <input type="text">
 <button>입력</button>
 <script>
  const number = parseInt(prompt('몇 명이 참가하나요?'),10);
  const $button = document.querySelector('button');
  const $input = document.querySelector('input');
  const $word = document.querySelector("#word")

  let word; //제시어
  let newword; //새로 입력한 단어
  const clickbutton = () => {
      if (!word) { //제시어가 비어있는가
        word = newword;
        $word.textContent= word; //Span에 word값 넣어주기
        $input.value = ''; //보통 textContent가 값에 해당함. value를 쓰는건 예외적
      }
      else {

      }
  }
  const inputword = (event) => {
      newword=event.target.value;
  }

  $input.addEventListener('input',inputword);
  $button.addEventListener('click',clickbutton);

 </script>

</body>
</html>
```
``` java
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>끝말잇기</title>
</head>
<body>
 <div><span id = 'order'>1</span>번째 참가자</div>
 <div>제시어: <span id = 'word'></span></div>
 <input type="text">
 <button>입력</button>
 <script>
  const people = parseInt(prompt("몇 명이 참가하나요?"),10);
  const $button = document.querySelector('button');
  const $input = document.querySelector('input');
  const $word = document.querySelector('#word');


  let word;
  let newword;

  $input.addEventListner = (event) => {
      newword = event.target.value;
  }  
  $button.addEventListner = () => {
      if (!word){
          word = newword;
          $word.textContent = word
          $input.value = '';
      }
  }

 </script>

</body>
</html>
```