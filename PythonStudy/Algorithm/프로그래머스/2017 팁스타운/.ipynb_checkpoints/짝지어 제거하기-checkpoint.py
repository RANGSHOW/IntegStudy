# 모두 제거 => return 1
# 모두 제거 불가 => return 0
def delete(s: str):
    if len(s) == 0:
        return 1
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1]:
            newString = s[0:i] + s[i + 2:]
            print(newString)
            return delete(newString)
            
    
    
def solution(s: str):
    resultStr = delete(s)
    if len(s) == len(resultStr):
        return -1
    elif len(resultStr) == 0:
        return 1
    else:
        return 0



if __name__ == "__main__":
    # sList = ['abba', 'cescffcsec', 'abc', 'bedaadebcc']
    # ansList = []

    s = 'abba'
    delete(s)
    # print(delete(s))
    
    