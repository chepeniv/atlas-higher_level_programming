#!/usr/bin/python3

def print_reversed_list_integer(a_list):
    length = len(a_list)
    for i in range(0, length):
        print("{:d}".format(a_list[length - i - 1]))
