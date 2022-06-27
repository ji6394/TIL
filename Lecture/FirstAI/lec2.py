def calculate_rectangle_area(x,y):
    result = x*y
    return result
calculate_rectangle_area(5,3)

def f(x):
    return 2*x+7


def g(x):
    return x**2

print(f(5)+g(8))
list_ex = [5,4,3,2,1]
sorted(list_ex) #원본 정렬 x
list_ex
list_ex.sort() #원본 정렬
list_ex

print('%s %s' %('one','two'))
print('Product: %10s, Price per unit: %10.1f' %('Apple', 5.243))

name = 'Jung Jihoon'
age = 25
print('My name is {0} and {1} years old.'.format(name, age))

#stack : list로 구현 가능
a=[1,2,3,4,5]
a.append(10)
a.append(20)
a.pop()
a.pop()

word = input('input a word : ')
word_list = list(word)
for _ in range(len(word_list)):
    print(word_list.pop())
    print(word_list)

#Queue : list로 구현 가능
a = [1,2,3,4,5]
a.append(10)
a.append(20)
a.pop(0)
a

t=(1,2,3)
type(t)

#set(집합) : 값을 순서없이 저장, 중복없음
s = set([1,2,3,4,5,6])
s.discard(3)
s

#deque

from collections import deque
deque_list = deque()
for i in range(5):
    deque_list.append(i)
deque_list.appendleft(10)
deque_list
deque_list.rotate(2)
deque_list

#join
colors = ['red','blue','green','yellow']
'-'.join(colors)

#pprint
import pprint #행별로 출력

#enumerate : 각 요소 별 번호와 함께 출력

#zip : 병렬 추출
alist = ['a1','a2','a3']
blist=['b1','b2','b3']

[[a,b] for a,b in zip(alist, blist)]