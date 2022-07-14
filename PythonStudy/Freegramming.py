class Person():
    def __init__(self):
        self.name = None
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

me = Person()
print(me.get_name())
me.set_name("ChangHyeon")
print(me.get_name())



import random as rd 

print(3 + 3)

print(pow(0.95,20))

def Person(object):
    pass

for i in range(0, 10):
    for j in range(0, 10):
        print("{} X {} = {}".format(i, j, i * j))
    print()


print(list(range(10, 0, -1)))

class Animal(object):
    def __init__(self):
        self.spices = "animal"
        
    def show_spices(self):
        return self.spices


for i in range(15):
    for j in range(15):
        print("{:2} X {:2} = {:3}".format(i, j, i * j))
    print()

    
print("Hello World!")
print("Sorry, I don't know what to do...")
import pandas as pd
my_array = pd.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(my_array)

testString = 'one3two'

def solution(string: str) -> str:
    answer = []
    for i in len(string):
        if string[i].isdigit() == True:
            answer.append(i)
        else:
            if string[i] == 'z':
                answer.append('0')
                # i의 위치 다시 잡기
            elif string[i] == 'o':
                answer.append('1')
                # i의 위치 다시 잡기    
            elif string[i] == 't': # two, three 구분
                if string[i + 1] == 'w':
                    answer.append('2')
                    # i의 위치 다시 잡기                  
                else:
                    answer.append('3')
                    # i의 위치 다시 잡기                  
                pass

string = 'zero3one3two3'
answer = []
for i in range(len(string)):
    print('i는 {}입니다.'.format(i))
    if string[i] == 'k':
        answer.append('케이')
        i
    else:
        pass
print(answer)


def solution(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')    
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    answer = int(s)
    return answer

print(solution('one4seveneight'))

string = 'one4seveneight'
string.replace('one', '1')
print(string)