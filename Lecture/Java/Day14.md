## Java 14강
#### 객체는 메모리에서 동적으로 생성되며 객체가 더 이상 필요 없어지면 GC(Garbage Collector)가 회수
#### 생성한 객체의 주소를 변수에 저장하는 것을 레퍼런스라고 한다.
``` java
Childclass class1 = new Childclass();
Childclass class2 = new Childclass();
Childclass class3 = new Childclass();
// Class1,2,3은 모두 레퍼런스
```
#### 자료형이 같아도 다른 공간에 존재하는 객체는 다른 객체
#### 레퍼런스에 null이 저장되면 객체의 연결이 끊기며 더 이상 객체를 이용할 수 없다.
#### 레퍼런스는 사라지지 않는다.