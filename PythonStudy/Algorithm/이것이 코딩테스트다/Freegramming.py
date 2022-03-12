from logging import root
from xml.dom import NoModificationAllowedErr

import pandas as pd
import random as rd

root_num = 20
for i in range(root_num):
    print("{} 번째 시도".format(i))
    rd.seed(i)
    for j in range(root_num):
        pass

    