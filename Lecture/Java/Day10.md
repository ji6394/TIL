## Java 10강
#### 반복문
- for
``` java
System.out.println("Input number : ");
Scanner scanner = new Scanner(System.in);
int num = scanner.nextInt();

for (int i = 1;i<10;i++){
    System.out.printf("%d * %d = %d\n",num,i,num*i);

}
```
- while
``` java
System.out.println("Input number : ");
Scanner scanner = new Scanner(System.in);
int num = scanner.nextInt();

int i = 1; //while은 for과 달리 미리 사용할 변수 선언돼있어야함
while (i<10){
    System.out.printf("%d*%d=%d\n",num,i,num*i);
    i++;
}
```
- do while : 최소 한번은 해당 동작문 실행
``` java
System.out.println("Input number : ");
Scanner scanner = new Scanner(System.in);
int num = scanner.nextInt();

int i = 1;
do {
    System.out.println("1번은 출력한다");
    i++;
} while(i<5);
```
