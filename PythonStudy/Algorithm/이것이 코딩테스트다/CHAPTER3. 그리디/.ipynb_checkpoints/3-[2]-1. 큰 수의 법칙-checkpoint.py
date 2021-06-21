# N: 주어지는 정수 리스트의 길이
# M: 더해지는 정수의 개수
# K: 더해지는 정수의 최대 연속되는 수

n, m, k = 5, 8, 3 
numList = [2, 4, 5, 4, 6]
    

numList.sort(reverse=True)
num1 = numList[0]
num2 = numList[1]

resultList = []
result = 0

while len(resultList) < m:
    for _ in range(k):
        resultList.append(num1)
    resultList.append(num2)
    
for num in resultList:
    result += num
    
print(result)
    

        