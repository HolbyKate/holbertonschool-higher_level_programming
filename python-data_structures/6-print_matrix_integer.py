#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return
    for raw in matrix:
        for column in raw:
            print("{:d}".format(column), end="")
            if column != raw[-1]:
                print(" ", end="")
        print()
