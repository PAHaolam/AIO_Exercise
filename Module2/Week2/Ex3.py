import numpy as np


def compute_cosine(v1, v2):
    dot_product = v1@v2
    norm_product = np.linalg.norm(v1)*np.linalg.norm(v2)
    result = dot_product/norm_product
    return result


print(compute_cosine(np.array([1, 2, 3, 4]), np.array([1, 0, 3, 0])))
