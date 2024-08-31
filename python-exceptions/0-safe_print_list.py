#!/usr/bin/python3

def safe_print_list(L=[], x=0):
    t = 0
    for i in range(0, x):
        try:
            print("{}".format(L[i]), end='')
            t += 1
        except (IndexError):
            break
    print("")
    return t
