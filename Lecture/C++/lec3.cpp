#include <iostream>
#include <vector>
#include <cmath>//수학적 연산을 도와주는 라이브러리
// https://www.youtube.com/watch?v=-TkoO8Z07hI
// typedef : 다른 데이터 타입의 추가적인 이름을 부여할 수 있도록 사용되는 reserved keyword. 가령 닉네임 같은것
// 가독성을 높이기 위해 사용함

typedef std::vector<std::pair<std::string, int>> pairlist_t; //일반적으로 typedef는 _t로 끝남

//using : typedef 대신 사용 가능. 이게 더 가독성 있는듯
using text_t = std::string;
using number_t = int;

namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}

int main(){
    // The const keyword : 변수의 값이 constant이므로 변경 불가능하게 함
    // Read Only!
    // const는 변수 제일 앞에 접두사로 입력. const 변수는 모두 대문자로 선언
    const double PI = 3.14159;
    const int LIGHT_SPEED = 299792458;
    const int WIDTH = 1920;
    const int HEIGHT = 1080;
    double radius = 10;
    double circumference = 2 * PI * radius;

    // Namespace : entity가 고유한 이름을 공유할 수 있도록 함.
    int x = 0;
    using namespace first; //namespace first를 사용하겠다!
    std::cout << x << '\n'; //따로 namespace지정해주지 않으면 로컬 변수에 해당하는 0값 리턴
    std::cout << first::x << '\n';
    std::cout << circumference << " cm" << '\n';


    //typedef
    pairlist_t pairlist;

    // arithmetic operations
    // ++ : 1만 더함
    // -- : 1만 뺌
    // 나머지는 파이썬과 유사

    //type conversion
    double y = (int) 3.14;
    std::cout<< y <<'\n';

    int correct = 8;
    int questions = 10;
    double score  = correct/(double)questions * 100;

    std::cout << score << "%" << '\n';
    //47:05
    // User input
    //cout << insertion operator
    //cin >> extraction operator 파이썬에서 input과 동일한 효과
    std::string name_1;
    std::cout << "What's your name?: ";
    std::cin >> name_1;

    std::cout << "Hello " << name_1;


    // useful math functions
    double umf1 = 3;
    double umf2 = 4;
    double z;

    z = std::max(umf1, umf2);




    return 0;
}