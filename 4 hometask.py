# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\n\t python task.py <имя_файла>")
        exit(1)

    matrix = []
    with open(sys.argv[1], "r", encoding = "utf-8") as fin:
        for line in fin:
            row_str = line.strip()
            if row_str:
                row = list(map(int, row_str.split()))
                matrix.append(row)

    new_matrix = []
    for row in matrix:
        if not all([value == 0 for value in row]):
            new_matrix.append(row)

    rows = len(new_matrix)
    cols = len(new_matrix[0])
    for row in matrix[1:]:
        assert len(row) == cols

    new_matrix_t = []
    for _ in range(cols):
        new_matrix_t.append([0]*rows)

    for i in range(rows):
        for j in range(cols):
            new_matrix_t[j][i] = new_matrix[i][j]

    new_matrix = []
    for row in new_matrix_t:
        if not all([value == 0 for value in row]):
            new_matrix.append(row)
    cols = len(new_matrix)
    new_matrix_t = []
    for _ in range(cols):
        new_matrix_t.append([0] * cols)

    for i in range(rows):
        for j in range(cols):
            new_matrix_t[i][j] = new_matrix[j][i]

    print(new_matrix)

