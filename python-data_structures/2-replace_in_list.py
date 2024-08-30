#!/usr/bin/python3

def replace_in_list(a_list, idx, value):
    if idx < 0 or idx > len(a_list) - 1:
        return a_list
    else:
        a_list[idx] = value
        return a_list
