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



def binarySearch(arr):
    index = 0
    arr.sort()

    
    


    return index











