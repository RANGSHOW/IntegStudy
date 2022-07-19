# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

def solution(id_list, report, k):
    report = list(set(report))  # 동일 신고 제거
    # 이중 for문 안쓰고 하는 법 생각해보기
    for id in id_list:
        temp = 0
        for reporter, reportee in report:
            if id == reportee:
                temp += 1
                
    answer = []
    return answer


aList = ["ryan con", "ryan con", "ryan con", "ryan con"]
