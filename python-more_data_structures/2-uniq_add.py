#!/usr/bin/python3

def uniq_add(L=[]):
    S = set(L)
    tot = 0
    for i in S:
        tot += i
    return tot
