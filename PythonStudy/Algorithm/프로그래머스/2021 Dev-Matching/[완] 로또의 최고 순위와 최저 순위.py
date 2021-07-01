lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]	
# answer = [3, 5]

def solution(lottos, win_nums):
    score = 0
    for myNum in lottos:
        if myNum in win_nums:
            score += 1
    poss = lottos.count(0)
    
    maxScore = score + poss
    minScore = score
    if minScore == 0:
        minPlace = 6
    else:
        minPlace = 7 - minScore
        
    answer = []
    answer.append(7 - maxScore)
    answer.append(minPlace)
    
    return answer
score = 0

print(solution(lottos, win_nums))