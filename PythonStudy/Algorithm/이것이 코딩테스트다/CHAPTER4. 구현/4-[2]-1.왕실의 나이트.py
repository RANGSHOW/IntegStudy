# 개요
    # 나이트가 이동할 수 있는 경우의 수 출력
    # 8 X 8 좌표
    # 가로(a~h), 세로(1~8)의 좌표로 표현
# 입력 예시
    # a1: 현재 나이트의 위치
# 출력 예시
    # 2: 나이트가 이동할 수 있는 2가지 경우 (c2, b3)
    

    
if __name__ == "__main__":
    knightMove = [2, -1], [2, 1], [-2, -1], [-2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2]
    
    currentPos = input()
    currentPos = [ord(currentPos[0]) - 96,  int(currentPos[1])]
    print(currentPos)
    possibleMoveCnt = 0
    
    for colMove, rowMove in knightMove:
        print("colMove: {} \nrowMove: {}".format(colMove, rowMove))
        newColPos = currentPos[0] + colMove
        newRowPos = currentPos[1] + rowMove
        print(newColPos, newRowPos)
        
        if 1 <= newColPos and newColPos <= 8 and 1 <= newRowPos and newRowPos <= 8:
            possibleMoveCnt += 1
            
    print(possibleMoveCnt)


    
    
    