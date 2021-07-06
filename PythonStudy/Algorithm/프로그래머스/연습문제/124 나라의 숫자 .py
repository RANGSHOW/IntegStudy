# 1, 2, 4 만 가지고 숫자를 표현
# 1 <= inputNum <= 500,000,000

from random import randint

def solution(num):
    answer = ''
    # 1, 2, 4를 0, 1, 2를 쓰는 3진수로 생각하고 변환

    return answer

if __name__ == "__main__":
    
    maxExpo = 0
    num = randint(1, 500000000)
    print("num:", num)
    while True:
        if pow(3, maxExpo) < num <= pow(3, maxExpo + 1):
            break
        else:
            maxExpo += 1
    numList = [0] * maxExpo
    cnt = 0
    while num != 0  or cnt < 10000:  # 곱해진 숫자를 빼면서 0이 되면 루프 종료
        cnt += 1
        for expo in range(maxExpo, -1, -1):
            for coeff in range(2, -1, -1):
                # 리스트 안에 들어갈 숫자 정하기
                # 정하고 pow(2, numList[i])
                if num >= coeff * pow(3, expo):
                    num -= coeff * pow(3, expo)
                    print(num)
                    numList[expo - 1] = coeff
    print(numList)
    print(cnt)