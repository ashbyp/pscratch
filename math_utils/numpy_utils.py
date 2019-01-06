import numpy as np


def get_random_int_array(size, seed=0):
    np.random.seed(seed)
    return np.random.randint(10, size=size)

