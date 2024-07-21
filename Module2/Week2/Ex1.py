import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = vector1@vector2
    return result


def matrix_multi_vector(matrix, vector2):
    result = matrix@vector2
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = matrix1@matrix2
    return result


def inverse_matrix(matrix):
    det = matrix[0, 0]*matrix[1, 1] - matrix[0, 1]*matrix[1, 0]
    if det == 0:
        return None
    result = np.array([[matrix[1, 1], - matrix[0, 1]],
                       [- matrix[1, 0], matrix[0, 0]]])/det
    return result
