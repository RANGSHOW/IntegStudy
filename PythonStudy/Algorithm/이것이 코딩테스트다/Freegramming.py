import random as rd
from unicodedata import name

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))
    print()


import random as rd
import pandas as pd
import numpy as np

my_string = 'abcde'
my_arr = np.asarray(my_string)
print(my_arr)

for i in range(100):
    for j in range(100):
        print("{} X {} = {}".format(i, j, i * j))
    print()
    

class Person():
    def __init__(self):
        self.name = None
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

