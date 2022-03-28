## Datatrend 강의1강
#### html에는 태그가 사용됨
#### 모든 태그는 <>로 시작하고 </>로 끝남
#### head 태그는 출력되지는 않지만 웹브라우저가 알고 있어야 할 정보들
#### body 태그는 화면에 출력될 내용
#### h1 태그 : h는 제목을 가리킴, 뒤의 숫자는 크기를 말함. 1이 가장큼, 6이 가장작음
#### 글 작성할 때는 문단 태그 안에 쓰기
#### 줄바꾸기는 <br>태그
#### list작성은 ol(ordered list)과 ul(unordered list)로 나누어짐
#### 각 list 앞에는 <li>리스트 태그 넣어주자
#### 해당 태그의 속성은 태그 안에 입력
#### align = "center" : 배치의 위치를 나타냄, center, left, right로 나누어짐
``` html
<html>
<head>
<title>첫 타이틀</title>
</head>
<body>
<h1 align = "center">html 플립러닝 수업</h1>
<h3>수업소개</h3>
<p>프로그래밍을 재미있고, <br>흥미롭게 접근할 수 있도록 하고자 합니다. 비 공대생이 프로그램이라는 새로운 영역을 호기심을 갖고, <br>큰 부담없이 들을 수 있도록 설계하였습니다. 프로그램 문법을 익히는 과정은 짧게 최소한의 문법만을 학습하도록 <br>구성하였습니다. 최소한의 문법적 지식으로 학습자의 머릿속에 있는 논리의 흐름을 프로그래밍 언어를 통해 시각적으로 <br>표현하고, 그 결과를 확인하는 프로그래밍 교육과정입니다.</p>
<h6>목록태그 소개</h6>
<ol>
<li>국어국문학과</li>
<li>영어영문학과</li>
<li>철학과</li>
</ol>
<ul>
<li>국어국문학과</li>
<li>영어영문학과</li>
<li>철학과</li>
</ul>
</body>
</html>
```
#### <!DOCTYPE html> <!~~ 은 주석문에 해당
#### <hr> : 선 긋기
#### 리스트 종류
- 순서 있는 리스트(ordered list) : <ol></ol>
- 순서 없는 리스트(unordered list) : <ul></ul>
- 정의형 리스트(definition list) : <dl></dl>
#### 리스트는 type, start 설정 가능
``` html
<ol type = '1'|'A'|'a'|'I'|'i'
    start = 'value'>
    <li>아이템</li>
</ol>
```
#### type는 마커의 종류, start는 마커의 시작점 설정
#### 리스트는 중첩도 가능
``` html
<dl>
    <dt><strong></strong> <!dt는 제목,strong은 진하게 표시>
    <dd> <!dd는 설명, 태그 하나로 구성>
</dl>
```
#### <br>태그를 쓰기 위해서는 &lt;br&gt;

#### 이미지, 링크 삽입하기
``` html
<html>
<head>
<title>이미지와링크</title>
<body>
<h1>이미지 삽입하기</h1>
<img src="한양.png"> ###이미지는 같은 디렉토리에 있어야 함
<h3>인문소프트웨어융합전공</h3>
<h1>링크태그 만들기</h1>
<a href="http://hycore.hanyang.ac.kr">미래인문학교육인증센터</a>
<br>
<br>
<br>
<h1>이미지링크</h1>
<a href="http://hycore.hanyang.ac.kr"><img src="한양.png" width = "100" height = "100"></a>
</body>
</head>
</html>