# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

def solution(id_list, report):
    report = list(set(report))  # ���� �Ű� ����
    # ���� for�� �Ⱦ��� �ϴ� �� �����غ���
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
print(solution(id_list, report))
print(solution(id_list, report))
print(solution(id_list, report))
print("cause it's weekend")
print("cause it's Sunday")