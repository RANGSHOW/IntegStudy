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