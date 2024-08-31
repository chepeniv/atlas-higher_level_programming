#!/usr/bin/python3

def multiply_by_2(D):
    E = D.copy()
    for k, v in E.items():
        E.update({k: v * 2})
    return E
