# 모두 제거 => return 1
# 모두 제거 불가 => return 0

from mmap import ACCESS_DEFAULT


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

    