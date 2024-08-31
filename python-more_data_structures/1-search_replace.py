#!/usr/bin/python3

def search_replace(L, S, R):
    M = L.copy()
    length = len(M)
    for i in range(0, length):
        if M[i] == S:
            M.pop(i)
            M.insert(i, R)
    return M
