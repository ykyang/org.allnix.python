import unittest

import numpy as np

class NumpyTest(unittest.TestCase):
    def test_arange(self):
        """Learn numpy.arange()
        """
        
        v: np.ndarray = np.arange(10)
        
        # 1 dim array
        self.assertEqual(1, v.ndim)
        # shape = (10,)
        self.assertEqual(1, len(v.shape))
        self.assertEqual(10, v.shape[0])
        self.assertEqual(10, v.size)

        l: list = list(range(0,10))
        self.assertTrue(np.array_equal(l, v))