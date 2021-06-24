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


