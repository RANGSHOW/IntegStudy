from random import randint

class Person(object):
    def __init__(self):
        self.lastName = "Kim"
        self.firstName = ""
    def setFirstName(self, firstName):
        self.firstName = firstName
    def getFullName(self):
        return self.firstName + ", " + self.lastName

me = Person()
me.setFirstName("Chang Hyeon")
print(me.getFullName())


import numpy as np
import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                columns=['kim', 'lee', 'park'], 
                index=['A' ,'B', 'C'])



for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))