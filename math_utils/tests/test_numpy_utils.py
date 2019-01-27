from unittest import TestCase
from math_utils import numpy_utils


class TestAllUtils(TestCase):

    def test_get_random_int_array(self):
        a = numpy_utils.get_random_int_array((3, 4, 5), 0)
        self.assertEqual(a.ndim, 3)
        self.assertEqual(a.shape, (3, 4, 5))
        self.assertEqual(a.size, 60)


