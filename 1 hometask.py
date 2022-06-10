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

    A.sort(key = lambda row: sum(x for x in row if (x > 0 and x % 2 == 0)))
    print(A)