# 이진탐색
# n, m (n: 떡의 개수, m: 요청한 떡의 길이)

# input 
n, m = 4, 6
dduck_list = [19, 15, 10, 17]  # sum(dduck_list) >= m
# output
# 절단기의 높이 (h)

# if h == 15
# => cut_list = [4, 0, 0, 2]

def binary_search(arr, target, start, end):
    mid = (start + end) // 2
    if get_customer_dduck(arr, mid) == target:
        return mid
    elif get_customer_dduck(arr, mid) > target:  # 잘린 길이가 더 길다 == 더 길게 잘라도 된다 == cut_size를 키운다
        if get_customer_dduck(arr, mid + 1) < target:
            return mid
        else:
            return binary_search(arr, target, mid + 1, end)
    else:  # 잘린 길이가 목표에 미치지 못한다 
        return binary_search(arr, target, start, mid - 1)

def get_customer_dduck(dd_list, cut_size) -> int:
    cus_dd = 0
    for dd in dd_list:
        temp = dd - cut_size
        if temp < 0:
            temp = 0
        cus_dd += temp
    return cus_dd

if __name__ == "__main__":
    dduck_list = [19, 15, 10, 17]
    m = 6
    answer = binary_search(dduck_list, m, 0, max(dduck_list))
    print(answer)

