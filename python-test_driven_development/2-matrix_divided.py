#!/usr/bin/python3
"""
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) and not isinstance(matrix[0], list):
        raise TypeError(msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if isinstance(element, (int, float)):
                new_row.append(round(element / div, 2))
            else:
                raise TypeError(msg)
        new_matrix.append(new_row)
    return new_matrix
