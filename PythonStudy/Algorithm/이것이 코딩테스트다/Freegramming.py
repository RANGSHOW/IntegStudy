import random as rd

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