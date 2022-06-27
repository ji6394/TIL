## Javascript 2-18
#### break : 반복문 멈추기
``` javascript
let i = 0;
while (true) {
    if (i===5) break;
    i++;
}
console.log(i)
```
#### continue : 이후 코드 뛰어넘기
#### 중첩된 반복문 사용
``` javascript
for (i=0 ; i < 5; i++)
    for (j=0 ; j < 5; j++)
      console.log(i,j)
```
#### 구구단 출력
``` javascript
for (i=1; i<10; i++)
  for (j=1; j<10; j++)
    console.log(i+'x'+j+'='+i*j)
```

#### 별 찍기
``` javascript
for (i=0;i<10;i++){
  if (i%2===0) continue;
  let n = ((9-i)/2);
  console.log(' '.repeat(n)+'*'.repeat(i)+' '.repeat(n));
}
```