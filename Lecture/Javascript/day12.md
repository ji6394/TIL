## Javascript 끝말잇기 게임 만들기
#### HTML : 화면의 구조
#### CSS : 스타일, 각 요소의 배치, 디자인
#### Javascript : 화면의 동작
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
  alert(number);
  const YesorNo = confirm('맞나요?')
 </script>

</body>
</html>
```
#### lan은 언어, title은 제목
#### shift + alt + 방향키 아래 : 해당 라인 복사
#### F5로 실행
#### prompt('문자열'): input과 같음.
#### alert() : 해당 요소 경고창에 출력
#### confirm('문자열'): 예, 아니오 값 입력받음