## Java 12강
#### 클래스 제작 : 클래스는 멤버 변수(속성), 메서드(기능), 생성자 등으로 구성된다.
``` java
public class Grandeur {
    public String color;
    public String gear;
    public int price;
    // 멤버 변수
    public Grandeur(){
        System.out.println("Grandeur constructor");
    }
    // 생성자 
    public void info(){
        System.out.println("--info--");
        System.out.println("color : " + color);
        System.out.println("gear : " + gear);
        System.out.println("price : "+price);
    }
    // 메서드
}
```
#### 객체 생성 : 클래스로부터 'new'를 이용하여 객체를 생성
``` java
Grandeur mycar1 = new Grandeur();
mycar1.color = "black";
mycar1.gear = "auto";
mycar1.price = 70000000;

mycar1.info();
```

#### 생성자 : 클래스에서 객체를 생성할 때 가장 먼저 호출
#### 생성자는 여러 개일수도, 생성자로 멤버 변수 설정할수도 있음
``` java
public class Bicycle{
    String color;
    int price;

    public Bicycle(){
        System.out.println("Bicycle constructor")
    }
    public Bicycle(String c, int p) {
        System.out.println("Bicycle constructor II")
        color = c;
        price = p;
    }
}
```
