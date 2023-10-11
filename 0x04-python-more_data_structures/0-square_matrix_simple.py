#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = [[x**2 for x in rows] for rows in matrix]
    return newMatrix
