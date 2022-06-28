#객체 지향 프로그래밍 : 클래스(설계도)와 인스턴스(실제 구현체)
from asyncio.windows_events import NULL


class SoccerPlayer(object):
    def __init__(self, name : str, position : str, back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number #속성 지정, self는 생성된 인스턴스를 말함
    def __str__(self):
        return 'Hello, My name is %s. My Back Number is %d' % (self.name, self.back_number)
    def __add__(self, other):
        return self.name + other.name
    def change_back_number(self, new_number):
        print('선수의 등번호를 변경합니다. From %d to %d' %(self.back_number, new_number))
        self.back_number = new_number
abc = SoccerPlayer('Son','FW',7)
kane = SoccerPlayer('Kane','FW',10)
abc is kane
print(abc)
abc+kane

#assignment
class Note(object):
    def __init__(self, content : None):
        self.content = content
    def write_content(self, content):
        self.content = content
    def remove_content(self):
        self.content = ''
    def __add__(self, other):
        return self.content + other.content
    def __str__(self):
        return self.content
class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes={}
    def add_note(self, note, page=0):
        if self.page_number <300:
            if page ==0:
                self.notes[self.page_number] = note
                self.page_number +=1
            else:
                self.notes = {page : note}
                self.page_number +=1
        else:
            print('Page가 모두 채워졌습니다')
    def remove_note(self, page_number):
        if page_number in self.note.keys():
            return self.notes.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않습니다')
    def get_number_of_pages(self):
        return len(self.notes.keys())
# 객체 지향을 위해 필요한 3가지
# 상속 : 부모클래스로부터 속성과 method를 물려받은 자식 클래스 생성
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date
# 다형성 : 같은 이름 메소드읜 내부 로직을 다르게 작성 
# 가시성 : 객체에 대한 접근 제한

#decorate
#First-class objects : 일등함수, 변수나 데이터 구조에 할당이 가능한 객체, 파이썬의 함수는 모두 일급함수
#Inner function : 함수안에 또다른 함수
def print_msg(msg):
    def printer():
        print(msg)
    printer()
print_msg('Hello, Python')
# decorator function : 복잡한 클로져 함수를 간단하게 표현
def star(func):
    def inner(*args, **kwargs):
        print('*'*30)
        func(*args, **kwargs)
        print('*'*30)
    return inner
@star
def printer(msg):
    print(msg)
printer('Hello')
