progress = [93, 30, 55]
speeds = [1, 30, 5]
# return = [2, 1]

progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# return = [1, 3, 2]

# 100%가 될 때까지 소요되는 시간을 리스트로 나타낸다
def returnCompleList(progress, speeds):
    compleList = []

    for prog, speed in zip(progress, speeds):
        cnt = 0
        while prog < 100:
            prog += speed
            cnt += 1
        compleList.append(cnt)
    return compleList

if __name__ == "__main__":
    returnCompleList(progress, speeds)
    print(returnCompleList(progress, speeds))

    


