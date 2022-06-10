# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = []
    i = 0
    j = 0
    while((i < len(a) - 1) or (j < len(b - 1))):
        if(a[i] <= b[j]):
            c.append(a[i])
            if i != len(a) - 1:
                i += 1
        else:
            c.append(b[j])
            if j < len(b) - 1:
                j += 1
    print(c)