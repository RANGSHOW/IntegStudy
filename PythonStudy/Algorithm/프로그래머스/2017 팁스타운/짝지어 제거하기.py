# 모두 제거 => return 1
# 모두 제거 불가 => return 0

def solution(s: str):
    answer = -1

    idx = 0
    while True:
        for i in range(len(s)):  # s의 길이가 짧아지면 out of range 에러
            if s[i] == s[i + 1]:
                s = s[0:i] + s[i + 1:]
                break

    if s == 0:
        answer = 1
    else:
        answer = 0

    return answer

if __name__ == "__main__":
    sList = ['abba', 'cescffcsec', 'abc', 'bedaadebcc']
    ansList = []
    for s in sList:
        ansList.append(solution(s))
    print(ansList)  # 1, 1, 0, 1
    for i in range(10):
        for j in range(10):
            print("{} X {} = {}".format(i, j, i * j))
    ansList = [1, 2, 3, 4, 5]


def binarySearch(arr, start, end, target):
    if start > end:
        return -1 

    mid = start + end // 2

    if arr[mid] > target:
        end = mid - 1
        return binarySearch(arr, start, end, target)
    elif arr[mid] < target:
        start = mid + 1
        return binarySearch(arr, start, end, target)
    else:
        return mid

arrList = [1, 4, 5, 8, 9, 10, 13, 14, 19, 20]
print(binarySearch(arrList, 0, len(arrList) - 1, 10))
for i in range(10):
    for j in range(10):
        pass


