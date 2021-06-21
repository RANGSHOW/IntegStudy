# 입력 예시
    # 5: N (0 <= N <= 23)
# 출력 예시
    # 11475: 00:00:00 ~ N:00:00 시각 중 3이 하나라도 포함되는 경우의 수
    
if __name__ == "__main__":
    n = int(input())
    
    cnt = 0
    
    for hour in range(0, n + 1):
        for minute in range(0, 60):
            for second in range(0, 60):
                time = str(hour) + str(minute) + str(second)
                if '3' in time:
                    cnt += 1
                    
    print(cnt)
                    