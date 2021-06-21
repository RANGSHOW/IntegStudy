# 개요
    # 공간 밖 이동은 무시
    # 시작 좌표: (1, 1)
# 입력 예시
    # 5:  공간의 크기 
    # R R R U D D: 이동 계획서 
# 출력 예시
    # 3 4 : 최종 도착할 x, y 좌표
        
if __name__ == "__main__":
    
    mapSize = int(input())
    movingPlan = input().split()
    
    rowLoc, colLoc = 1, 1
    
    for singleMove in movingPlan:
        
        if singleMove == 'U':
            if rowLoc == 1:
                pass
            else:
                rowLoc -= 1
                
        elif singleMove == 'D':
            if rowLoc == mapSize:
                pass
            else:
                rowLoc += 1
                
        elif singleMove == 'R':
            if colLoc == mapSize:
                pass
            else:
                colLoc += 1
                
        else: 
            if colLoc == 1:
                pass
            else:
                colLoc -=1
                
    print(rowLoc, colLoc)
            
            
        
    

