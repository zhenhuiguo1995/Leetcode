def circle(row, col, row_length, col_length, matrix):
    seen = []
    res = []
    i, j = row, col
    while  j < col + col_length:
        if (i, j) not in seen:
            seen.append((i, j))
            res.append(matrix[i][j])
        j += 1
    j -= 1
    i += 1
    while i < row + row_length:
        if (i, j) not in seen:
            seen.append((i, j))
            res.append(matrix[i][j])
        i += 1
    i -= 1
    j -= 1
    while j >= col:
        if (i, j) not in seen:
            seen.append((i, j))
            res.append(matrix[i][j])
        j -= 1
    j += 1
    i -= 1
    while i > row:
        if (i, j) not in seen:
            seen.append((i, j))
            res.append(matrix[i][j])
        i -= 1
    return res


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

res = circle(0, 0, 3, 4, matrix)
print(res)