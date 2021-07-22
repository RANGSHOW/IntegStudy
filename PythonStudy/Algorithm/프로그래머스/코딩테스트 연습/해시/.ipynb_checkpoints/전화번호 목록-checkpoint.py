# 접두사인 경우 false, 접두사가 아니면 true

phone_book = ["12","123","1235","567","88"]
answer = False

def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                answer = False
    return answer