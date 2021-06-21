numList = ['1924', '1231234', '4177252841']
kList = [2, 3, 4]
returnList = ['94', '3234', '775841']

number = "2848571899"
k = 4
# return = "9999"

# 빼는 것이 아니라 정해진 자릿수만큼 순서에 맞게 뽑는 걸로 생각

answerNum = len(number) - k

answerList = []

while len(answerList) == answerNum:

    numberList = sorted(list(number), reverse=True)

    for i in numberList:
        bigNumIndex = number.find('%s' % i)
        if len(number[bigNumIndex:]) >= len(answerList):
            pass
        else:
            mber.
            continue
            nu