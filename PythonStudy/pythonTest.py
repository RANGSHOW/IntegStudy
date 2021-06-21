def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = [1, 3, 4, 6, 2, 8, 7, 9, 5]
    print(arr)
    bubbleSort(arr)
    print(arr)
    