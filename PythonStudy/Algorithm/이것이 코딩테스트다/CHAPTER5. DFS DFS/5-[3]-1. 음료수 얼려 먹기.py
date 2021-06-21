from pprint import pprint

# N X M 크기의 얼음틀
# 0: 구멍, 1: 칸막이

# n, m = 15, 14
# n, m = map(int, input().split())

# mold = [
#     '00000111100000',
#     '11111101111110',
#     '11011101101110',
#     '11011101100000',
#     '11011111111111',
#     '11011111111100',
#     '11000000011111',
#     '01111111111111',
#     '00000000011111',
#     '01111111111000',
#     '00011111111000',
#     '00000001111000',
#     '11111111110011',
#     '11100011111111',
#     '11100011111111']

n, m = 4, 4  # n: row, m: col

mold = [
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 1]]

# return = 5
iceList = []


# DFS 

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
            


if __name__ == "__main__":
    # 전체를 돌면서 0이 나오면 거기서 퍼져나간다
    # 일단 0의 갯수만큼 returnCnt 를 주고 연결된 걸 하나씩 뺀다
    
    for i in range(n):
        for j in range(m):
            if (mold[i][j] == 0):
                pass
            
            
                
                
                
                