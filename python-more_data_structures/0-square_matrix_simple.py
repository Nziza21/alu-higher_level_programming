#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers in a 2D matrix."""
    return [[value ** 2 for value in row] for row in matrix]
