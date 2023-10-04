#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mapped_matrix = [list(map(lambda x: x ** 2, raw)) for raw in matrix]
    return (mapped_matrix)
