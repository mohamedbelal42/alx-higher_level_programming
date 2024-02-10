#!/usr/bin/python3
"""Module for matrix divided method."""

def matrix_divided(matrix, div):
    """divides all elements of matrix by div.

    Args:
        matrix: list of lists containing int or float.
        div: number to divide matrix by.
    Raises:
        TypeError: if matrix is not list of lists containing int or float.
        TypeError: if sublists are not all the same size.
        TypeError: if div is not int or float.
        ZeroDivisionError: if div is zero.
    Return:
        list: list of lists representing divided matrix.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
