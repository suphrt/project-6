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
    k = 0
    for i in range(0, n - 1):
        for j in range(0, m - 1):
            if (A[i][j] == min(A[i][j],
                               A[i - 1][j - 1] * ((i > 0) and (j > 0)) + 1e6 * ((i <= 0 or (j <= 0))),
                               A[i - 1][j] * (i > 0) + 1e6 * (i <= 0),
                               A[i - 1][j + 1] * ((i > 0) and (j < n - 1)) + 1e6 * ((i <= 0) or (j >= n - 1)),
                               A[i][j - 1] * (j > 0) + 1e6 * (j <= 0),
                               A[i][j + 1] * (j < n - 1) + 1e6 * (j >= n - 1),
                               A[i + 1][j - 1] * ((i < n - 1) and (j > 0)) + 1e6 * ((i >= n - 1) or (j <= 0)),
                               A[i + 1][j] * (i < n - 1) + 1e6 * (i >= n - 1),
                               A[i + 1][j + 1] * ((i < n - 1) and (j < n - 1)) + 1e6 * ((i >= n - 1) or (j >= n - 1)))):
                print(A[i][j])
                k += 1
    print("k =", k)
