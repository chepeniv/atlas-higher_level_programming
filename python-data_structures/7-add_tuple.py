#!/usr/bin/python3

def add_tuple(a=(), b=()):
    L = [0, 0]

    for i in range(0, len(a)):
        if i < 2:
            L[i] += a[i]
        else:
            break
    for i in range(0, len(b)):
        if i < 2:
            L[i] += b[i]
        else:
            break

    ab = (L[0], L[1])
    return ab
