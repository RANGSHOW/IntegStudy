# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

def solution(id_list, report):
    report = list(set(report))  # 동일 신고 제거
    # 이중 for문 안쓰고 하는 법 생각해보기
    for i in range(len(id_list)):
        answer = [0] * len(id_list)
        temp = 0
        for single_repo in report:
            print((single_repo.split(" "))[1])
            if id_list[i] == (single_repo.split(" "))[1]:
                temp += 1
        answer[i] = temp
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(id_list, report))

for i in range(10):
    for j in range(10):
        print("{} X {} = {}".format(i, j, i * j))
    print()
