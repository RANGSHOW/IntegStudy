rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]   
    # (2, 2) 에서 (5, 4) 모양의 사각형을 회전 (내부는 그대로)
result = [8, 10, 25]

# 1. 실제로 queries[0] 부터 회전을 시켜서 맵을 저장
#   1.1 회전시키면서 해당 사각형의 변수를 하나씩 받아올 때 대소 비교

graph = [[x for x in range(rows)] for _ in range(columns)]



