def solution(s, n):
    answer = ''
    tempArr = []
    for char in s:
        if ord(char) == 32:
                tempArr += ' '
        else:
            if 65 <= ord(char) <= 90:  # 대문자인 경우
                if 90 < ord(char) + n :
                    tempArr.append(chr(ord(char) + n - 26))
                else: 
                    tempArr.append(chr(ord(char) + n))
            else:                      # 소문자인 경우
                if 122 < ord(char) + n :
                    tempArr.append(chr(ord(char) + n - 26))
                else:
                    tempArr.append(chr(ord(char) + n))
    answer = ''.join(tempArr)

    return answer

if __name__ == "__main__":
    inputString = "AaZz"
    num = 25
    resultString = solution(inputString, num)
    print(resultString)


