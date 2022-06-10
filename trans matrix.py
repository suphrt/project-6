# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = int(input("n - "))
    m = int(input("m - "))
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)
    print(A)
    B = []
    for _ in range(m):
        B.append([0]* n)
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    print(B)