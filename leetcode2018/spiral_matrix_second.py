n = 4
matrix = [[0 for _ in range(n)] for _ in range(n)]
temp = list(range(1, n**2 + 1))
index = 0

def fill_circle(row, col, row_length, col_length, index = 0):
    i, j = row, col
    while j < col + col_length:
        matrix[i][j] = temp[index]
        j += 1
        index += 1
    j -= 1
    i += 1
    while i < row + row_length:
        matrix[i][j] = temp[index]
        i += 1
        index += 1
    i -= 1
    j -= 1
    while j >= col:
        matrix[i][j] = temp[index]
        j -= 1
        index += 1
    j += 1
    i -= 1
    while i > row:
        matrix[i][j] = temp[index]
        i -= 1
        index += 1

fill_circle(0, 0, 4, 4, 0)
fill_circle(1, 1, 2, 2, 12)
print(matrix)

    