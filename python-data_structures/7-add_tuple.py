#!/usr/bin/python3

def add_tuple(a=(), b=()):
    L = [0, 0]

    for i in range(0, len(a)):
        L[i] += a[i]
        if i >= 1:
            break
    for i in range(0, len(b)):
        L[i] += b[i]
        if i >= 1:
            break

    ab = (L[0], L[1])
    return ab
