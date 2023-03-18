#include <iostream>

int main(){
    int x; //변수 선언
    x = 5; //변수 할당
    int y = 6;
    int sum = x+y;
    //integer(Whole number)
    int age = 21;
    int year = 2023;
    int days=7.5;//integer로 선언했기에 소수점은 날아감

    //double(number including decimal(소수))
    double price = 10.99;
    double gpa = 4.5;
    double temperature = 13.2;

    //char(single character)
    char grade = 'A';
    char initial = 'B';

    //bool(true of false)
    bool student = true;
    bool power = false;

    //string (objects that represents a sequence of text)
    std::string name = "Jung";
    std::string day = "Friday";
    std::string food = "Pizza";

    std::cout << x << '\n';
    std::cout << y << '\n';
    std::cout << sum << '\n';
    std::cout << days << '\n';
    std::cout << price << '\n';
    std::cout << grade << '\n';
    std::cout << name << '\n';
    std::cout << food << '\n';
    std::cout << "Hello? " << name << '\n';
    std::cout <<"You are " << age << " years old";
    return 0;
}