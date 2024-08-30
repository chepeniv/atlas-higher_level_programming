#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) > 0:
        for a in matrix:
            length = len(a) - 1
            for i in range(0, length):
                print("{:d}".format(a[i]), end=' ')
            print("{:d}".format(a[length]))
    else: 
        print("")
