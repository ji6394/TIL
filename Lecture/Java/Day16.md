## Java 16강
#### 패키지 : 클래스를 폴더 형식으로 관리
#### 패키지느 이름은 중복 방지, 이름만으로 내용이 예상되도록 만들기
#### 다른 패키지의 클래스를 사용하기 위해서 import 사용
#### import할 때 해당 패키지의 풀 네임 따오기
``` java
package com.java.main;

import com.java.dailyJournal.Dailyjournal;
import com.java.employee.Employee;
```
#### 클래스의 속성과 메서드에 static 키워드를 사용하면 어디서나 속성과 메서드를 공유할 수 있다.
``` java
/// 클래스 생성
package bank;

public class bank {
    String name;
    static int amount = 0 /// static으로 객체 간 공유 가능한 amount 변수 생성
    
    public bank(String name){
        this.name = name;
    }
    public void saveMoney(int money){
        amount += money;
        System.out.println("amount : "+amount);
    }
    public void spendMoney(int money){
        amount -= money;
        System.out.println("amount : "+amount);
    }
}
```
``` java
package practice;
import bank.bank;
    public static void main(String[] args) { ///메인메서드를 사용하지 않으면 해당 객체 생성에서 오류
    bank parkbank = new bank("박찬호");
    parkbank.saveMoney(100);

    bank leebank = new bank("이승엽");
    leebank.saveMoney(300);

    parkbank.spendMoney(300)

}
```



