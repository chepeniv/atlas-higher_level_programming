#!/usr/bin/python3

def square_matrix_simple(M=[]):
    N = []
    for a in M:
        b = map(lambda n: n * n, a)
        N.append(list(b))
    return N

