# Ax + By + C = 0 로 표현할 수 있는 n 개의 직선의 교점 중 정수 좌표에 별을 그리려고 한다

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	
    # line은 matrix 형태 세로(행) 2 ~ 1000, 가로 3 (A, B, C)
result = ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
    # 모든 별(교점)을 나타낼 수 있는 최소 사각형을 return 

# def solution(line):
#     answer = []
#     return answer

# A, B, C는 -100,000 이상 100,000 이하인 정수

def solution(line):
    for dotList in line:
        pass
        # 
    answer = []
    return answer

# 일단 두 선분이 주어졌을 때 생기는 교점을 return 하는 함수

p1 = line[0]
p2 = line[1]

print(p1)
for y in range(-100000, 100000):
    for x in range(-100000, 100000):
        if x != 0 and y != 0:
            if line[0][0]*x + line[0][1]*y + line[0][2] == line[1][0]*x + line[1][1]*y + line[1][2]:
                print("x = {} , y = {}".format(x, y))



def intersectionPoint(lists):
    pass
    # lists = [(a1, b1, c1), (a2, b2, c2)]
    


print("Finish")
print("***********")
print("********__*")
print("********__*")
