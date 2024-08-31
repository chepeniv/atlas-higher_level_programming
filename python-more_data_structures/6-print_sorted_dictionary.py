#!/usr/bin/python3

def print_sorted_dictionary(D):
    keys = D.keys()
    keys = list(keys)
    keys.sort()
    for k in keys:
        print("{}: {}".format(k, D.get(k)))
