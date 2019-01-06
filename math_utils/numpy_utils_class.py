from .numpy_utils import get_random_int_array


class NumpyUtils(object):

    def __init__(self, seed):
        self.seed = seed

    def get_random_int_array(self, size):
        return get_random_int_array(size, seed=self.seed)


