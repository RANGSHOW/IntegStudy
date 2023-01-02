# 2차원 배열을 시계 방향으로 90도 회전

def rotate_matrix_90_degree(arr):
    row_length = len(arr)
    col_length = len(arr[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = arr[r][c]

    return res

print('2')
# null

def sum(num1, num2): 
    return num1 + num2

if __name__ == "__main__":
    print(sum(2, 3))