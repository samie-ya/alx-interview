#!/usr/bin/python3
"""This script will rotate matrix"""


def rotate_2d_matrix(matrix):
    """This function will rotate a matrix"""
    matrix.reverse()
    mat = [[matrix[j][i] for j in range(len(matrix[i]))]
           for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = mat[i][j]
