rows = 5
columns = 5
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]   
    # (2, 2) 에서 (5, 4) 모양의 사각형을 회전 (내부는 그대로)
result = [8, 10, 25]

# 1. 실제로 queries[0] 부터 회전을 시켜서 맵을 저장
#   1.1 회전시키면서 해당 사각형의 변수를 하나씩 받아올 때 temp 변수로 대소 비교

graph = [[i + columns * j for i in range(1, rows + 1)] for j in range(columns)]


print(graph)

def rotateAndRtnMin(query):
    minRst = 0
    
    

    return minRst


class Person(object):
    def __init__(self):
        self.name = "Kim"
    def show_name(self):
        return self.name
    


if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            print("{} X {} = {}".format(i, j, i * j))

            