## Java 13강
#### 메서드도 변수와 같이 선언 및 정의 후 필요시에 호출에서 사용한다
``` java
public String name;
public String gender;
public int age;

public childClass(){
    System.out.println("--childClass constructor--")
}

public void setinfo(String n, String g, int a){
    System.out.println("--setinfo() start--")
    name = n;
    gender = g;
    age = a;
}
public void getinfo(){
    System.out.println("--getinfo() start--")
    System.out.println("name :" + name)
    ...
}


childClass child1 = new childClass;
child1.setinfo("hong gildong","M",25)
chidl1.getinfo()
```
#### 이름은 같고 매개변수의 개수 또는 타입이 다른 메서드를 만들 수 있다
#### 메서드를 호출할 때 접근자에 따라서 호출이 불가할 수 있다.
#### 접근자의 종류에는 크게 private과 public이 있는데 private의 경우 위 조건에 해당한다.