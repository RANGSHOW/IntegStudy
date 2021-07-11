# return = 2  

# scovile 안의 정수가 모두 k 이상 되게 연산
# 연산 방법 가장 낮은 두 스코빌을 골라서 (최저 + 차저 * 2)로 맵핑
# [1, 2, 3, 9, 10, 12] => [5, 3, 9, 10, 12]


def solution(scovile:list, k) -> int:
    count = 0
    while min(scovile) < k:
        mapping(scovile, k)
        count += 1
    return count

def mapping(scov: list, k):
    scov.sort()
    minNum1 = scov.pop(0)
    minNum2 = scov.pop(0)
    newNum = minNum1 + minNum2 * 2
    scov.append(newNum)
        
if __name__ == "__main__":
    count = 0
    scovile = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scovile, k))
    