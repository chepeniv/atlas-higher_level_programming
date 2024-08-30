#!/usr/bin/python3

def add_tuple(a=(), b=()):
    l = [0, 0]
    
    for i in range(0, len(a)):
        if i < 2:
            l[i] += a[i]
        else:
            break
    for i in range(0, len(b)):
        if i < 2:
            l[i] += b[i]
        else:
            break

    ab = (l[0], l[1])
    return ab
