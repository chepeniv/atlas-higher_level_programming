#!/usr/bin/python3

def safe_print_list_integers(L=[], x=0):
    total = 0

    for i in range(0, x):
        try:
            print("{:d}".format(L[i]), end='')
            total += 1
        except (TypeError, ValueError):
            continue
        #except (IndexError):
        #    break
    print("")
    return total
