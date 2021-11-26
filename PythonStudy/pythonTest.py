def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def dfs(graph, v, visited):
    visited[v] = True;


for i in range(10):
    for j in range(10):
        print("{:2} X {:2} = {:2}".format(i, j, i * j))


aList = [1, 2, 3]
bList = aList

print("id(aList): {}\nid(bList): {}".format(id(aList), id(bList)))
if aList == bList:
    print("aList 와 bList는 값이 같다")
if aList is bList:
    print("aList 와 bList는 정체성이 같다")


aList = [1, 2, 3]
bList = aList.copy()

print("id(a): {} \nid(b): {}".format(id(aList), id(bList)))
if aList == bList:
    print("aList 와 bList는 값이 같다")
if aList is bList:
    print("aList 와 bList는 정체성이 같다")

bList.append(4)
    # 다른 객체에 바인딩 되어 id(aList) != id(bList)


# 클래스 생성, 상속 연습
class Person(object):
    def __init__(self):
        self.legNum = 2
        self.armNum = 2
        self.gender = "male or female..."
        self.job = 'null'

    def showGender(self):
        return self.gender

class Student(Person):
    def __init__(self):
        super().__init__()  # 슈퍼 클래스의 __init__() 메소드를 얻어온다 
        self.job = 'Student'  # 서브 클래스의 __init__() 메소드에 프로퍼티 추가

    def showGender(self):
        return super().showGender() + " " + "Guess what!"
    

me = Student()
print(me.showGender())
print(me.job)


aList = [1, 2, 3]
bList = [1, 2, 3]

print(aList == bList)
print(aList is bList)
print("{} \n{}".format(id(aList), id(bList)))

arrList = [1, 2, 3, 4]
for elem in arrList:
    print(elem)


arrList = [1, 2, 3, 4, 5, 6]

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))


for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))




def binarySearch(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, end)


from random import randint

num = 30
arrList = [0, 1, 3, 3, 6, 11, 15, 17, 21, 24, 24, 26, 26, 27, 27, 
           30, 31, 33, 34, 35, 38, 40, 44, 47, 48, 50, 51, 52, 53, 56]

print("array: ", arrList)
count = 0
target = arrList[11]
result = binarySearch(arrList, target, 0, len(arrList) - 1)
print(result)
names = ['']

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))

class Person(object):
    def __init__(self):
        self.spices = "human"
    def showSpices(self):
        return self.spices
    def __add__(self, other):
        return self.spices + other.spices
print(Person.__dir__)


from random import randint
import numpy as np
import pandas as pd

myDataFrame = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(myDataFrame)

from random import randint


def showName(object):
    return object.name

class People(object):
    def __init__(self, last_name):
        self.first_name = "rangshow"
        self.last_name = last_name
        self.name = self.first_name + " " + last_name

me = People("Kim")
print(showName(me))


for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        pass

from random import randint 

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))

def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = start + end // 2
    if arr[mid] > target:
        end = mid - 1
        
        return binary_search(arr, start, end, target)
    elif arr[mid] < target:
        start = mid + 1
        return binary_search(arr, start, end, target)
    else:
        return mid

import random 

my_list = [1, 8, 2, 7, 4, 3, 6, 5, 9, 10, 12, 14, 13, 11]

my_list.sort()

print(my_list)
target = 3
idxOfTarget = binary_search(my_list, 0, len(my_list) - 1, target)

print("target: {}\nresult: {}".format(target, my_list[idxOfTarget]))


def binarySearch(arr):
    

    for i in range(10):
        for j in range(10):
            print("{} X {} = {}".format(i, j, i * j))
        print()
    
    return
    
myList = [1, 2, 3, 4, 5]

myList.append(6)


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


def binary_search(start, end, target, arr):
    if start > end:
        return -1
    mid = start + end / 2
    if arr[mid] > target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1
    else:
        return 1

def rotate_matrix_90_degree(arr):
    row_length = len(arr)
    col_length = len(arr[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = arr[r][c]

    return res

def show_arr(arr):
    row_length = len(arr)
    col_length = len(arr[0])

    for r in range(row_length):
        for c in range(col_length):
            print(arr[r][c], end=' ')
        print()

if __name__ == "__main__":
    my_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    show_arr(my_arr)
    print()
    show_arr(rotate_matrix_90_degree(my_arr))


class OddCounter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            t = self.start
            self.start += 2
            return t

        raise StopIteration


# 7-4.py 한 줄 입력받아 출력하는 소스코드
import sys
input_data = sys.stdin.readlines().rstrip()
print(input_data)


print("Hello World!")



def counter_odd_number(num):
    res = 0
    for i in range(1, num + 1):
        if i // 2 != 0:
            res += 1
    return res

def counter_even_number(num):
    res = 0
    for i in range(1, num + 1):
        if i // 2 != 0:
            res += 1
    return res

print(counter_odd_number(5))

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))
    print()
    
import keras


