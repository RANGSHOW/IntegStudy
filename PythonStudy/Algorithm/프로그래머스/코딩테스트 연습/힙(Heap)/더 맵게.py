scovile = [1, 2, 3, 9, 10, 12]
k = 7
# return = 2  

# scovile 안의 정수가 모두 k 이상 되게 연산
# 연산 방법 가장 낮은 두 스코빌을 골라서 (최저 + 차저 * 2)로 맵핑
# [1, 2, 3, 9, 10, 12] => [5, 3, 9, 10, 12]

def mapping(scov, k):
    # 최소한의 움직임을 위해서 최소와 다음 수의 맵핑이 딱 k이상이 되게 만들기 
    scov.sort()
    for i in range(len(scov)):
        pass
        
if __name__ == "__main__":
    print(mapping(scovile, k))