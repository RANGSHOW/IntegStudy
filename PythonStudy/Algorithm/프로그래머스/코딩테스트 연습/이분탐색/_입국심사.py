# n	times	return
# 6	[7, 10]	28

# 가장 첫 두 사람은 바로 심사를 받으러 갑니다.

# 7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.

# 10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.

# 14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.

# 20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 
# 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 
# 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

n = 6
times = [7, 10]

# 일단 무조건 times 중 짧은 시간의 배수로 return 된다

capacityList = [0] * len(times)

import numpy as np

myArr = np.array((1, 2, 3))

print(myArr)