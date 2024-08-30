#!/usr/bin/python3

def new_in_list(old_list, idx, value):
    new_list = old_list.copy()
    if idx >= 0 and idx < len(old_list):
        new_list[idx] = value
    return new_list
