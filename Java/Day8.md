## Java 8강
#### 배열을 구성하는 데이터의 자료형에 따라 배열의 크기가 달라진다
#### 기본 자료형을 담고 있는 변수와 달리 배열 변수는 배열 데이터의 주소를 담고 있다.
``` java
int[] arr1 = {10,20,30,40,50};
int[] arr2 = null;
int[] arr3 = null;

//배열의 길이
System.out.println(arr1.length);

//배열의 요소 출력하기
System.out.println(Arrays.toString(arr1));

//배열 요소 복사하기
arr3 = Arrays.copyOf(arr1,arr1.length);
System.out.println(Arrays.toString(arr3));
//배열 레퍼런스
arr2 = arr1;
System.out.println(Arrays.toString(arr2));
```
#### 다차원 배열 역시 만들 수 있음
``` java
int[][] arrmul = new int[3][2];
arrmul[0][0]=10;
...
```
