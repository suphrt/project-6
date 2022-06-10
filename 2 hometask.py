# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = 3
    m = 3
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)
    B = []
    for _ in range(m):
        B.append([0]* n)
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    C = []
    cnt = 0
    for row in A:
        if A[row] in B:
            C = [x for x in row]
            print(C)
