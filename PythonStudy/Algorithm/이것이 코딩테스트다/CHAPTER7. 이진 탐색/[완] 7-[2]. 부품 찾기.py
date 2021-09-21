# 정수 n
# n 개의 정수 list (1 <= n <= 100,000,000)
# 정수 m
# m 개의 정수 list (1 <= m <= 100,000,000)

# 출력: 'yes' or 'no' 로 구성된 m 개의 list

# return: no yes yes

def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    elif arr[mid] == target:
        return 1
    else:
        return binary_search(arr, target, mid+1, end)

def search_parts(stock_list, order_list) -> list:
    res = []
    stock_list.sort()
    for part in order_list:
        if binary_search(stock_list, part, 0, len(stock_list)-1) == 1:
            res.append('yes')
        else:
            res.append('no')
    return res

if __name__ == "__main__":
    stock_num = 5
    stock_list = [8, 3, 7, 9, 2]
    order_num = 3
    order_list = [5, 7, 9]
    print(search_parts(stock_list, order_list))


    