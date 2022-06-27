## Java 9강
#### 조건문
- 양자택일(주로 if문)
``` java
int num1 = 10;
int num2 = 20;

if (num1>num2){
    System.out.println("a")
} else if (num1 == num2){
    System.out.println("b")
} else{
    System.out.println("c")
}
```
- 다자택일(주로 switch문)
``` java
System.out.println("점수를 입력하시오 : ");
Scanner inputnum = new Scanner(System.in);
int score = inputnum.nextInt();

switch (score) {
    case 90 :
      System.out.println("수");
      break;
    case 80 :
      System.out.println("우");
      break;
    case 70 :
      System.out.println("미");
      break;
    case 60 :
      System.out.println("양");
      break;
    case 50 :
      System.out.println("가");
      break;
}
inputnum.close();
```