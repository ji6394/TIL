## Java 15강
#### 디폴트 생성자 : 객체가 생성될 때 가장 먼저 호출되는 생성자
#### 만약 디폴트 생성자를 명시하지 않아도 컴파일 시점에 자동 생성된다.
``` java
public ObjectEx(){
    System.out.println("Default Constructor") //디폴트 생성자
}
```
#### 사용자 정의 생성자 : 디폴트 생성자 외에 특정 목적에 의해 개발자가 만든 생성자. 매개변수에 차이가 있음
``` java
 public ObjectEx(int i){
    System.out.println("UserDefined constructor");
    num=i;
}

ObjectEx obj2 = new ObjectEx(10);
```
``` java
public ObjectEx(String s, int i[]){
    System.out.println("UserDefined constructor");
    str = s;
    nums = i;
}

int arr[] = {10,20,30};
ObjectEx Obj3 = new ObjectEx("Java", arr);
```
#### 소멸자 : 객체가 GC에 의해서 메모리에서 제거될 때 finalize()메서드가 자동 호출됨
#### System.gc() : 가급적 빨리 GC가 작동하도록 요청
#### 현재 객체를 가리킬 때 this 사용
``` java
int num;
String str;
int nums;

public ObjectEx(int i, String s, int is[]) {
    System.out.println("UserDefined Constructor");

    this.num = i;
    this.str = s;
    this.nums = is;
}
```