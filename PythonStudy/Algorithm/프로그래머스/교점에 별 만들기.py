# Ax + By + C = 0 �� ǥ���� �� �ִ� n ���� ������ ���� �� ���� ��ǥ�� ���� �׸����� �Ѵ�

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	
    # line�� matrix ���� ����(��) 2 ~ 1000, ���� 3 (A, B, C)
result = ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
    # ��� ��(����)�� ��Ÿ�� �� �ִ� �ּ� �簢���� return 

# def solution(line):
#     answer = []
#     return answer

# A, B, C�� -100,000 �̻� 100,000 ������ ����

def solution(line):
    for dotList in line:
        pass
        # 
    answer = []
    return answer

# �ϴ� �� ������ �־����� �� ����� ������ return �ϴ� �Լ�

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
