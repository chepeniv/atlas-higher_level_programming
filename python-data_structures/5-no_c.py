#!/usr/bin/python3

def no_c(old_list):
    new_list = ""
    for char in old_list:
        if char != 'c' and char != 'C':
            new_list += char
    return new_list
