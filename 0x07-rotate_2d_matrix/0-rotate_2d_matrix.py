#!/usr/bin/python3
"""
Define a function that rotate
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90
    Args:
        matrix (list): 2d square matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp