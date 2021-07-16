prioritiesList = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
locationList = [2, 1]
returnList = [0, 5]

# 1. priorites 맨 앞에 있는 문서 꺼냄
# 2. 나머지 인쇄 대기 목록에서 해당 문서보다 중요도가 높은 (숫자가 큰) 문서가 한 개라도 존재하면 맨 뒤로 보낸다
# 3. 그렇지 않으면 해당 문서를 인쇄한다
# 4. location에 있는 문서의 인쇄 순서를 return 한다


priorities = prioritiesList[0]
location = locationList[0]

def solution(priorities: list, location):
    priorities.pop(0)
    answer = 0
    return answer




