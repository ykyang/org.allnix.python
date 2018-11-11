import unittest

from tests import cout, coutln
import numpy as np


class NumpyTest(unittest.TestCase):
    def test_zeros(self):
        """
        Learn numpy.zeros()

        python -m unittest tests.test_numpy.NumpyTest.test_zeros
        """
        v: np.ndarray = np.zeros((5,), dtype=float, order='C')
        coutln(v)


    def test_arange(self):
        """
        Learn numpy.arange()

        python -m unittest tests.test_numpy.NumpyTest.test_arange
        """

        v: np.ndarray = np.arange(10)
        coutln('>>> np.arange(10)')
        coutln(v)
        coutln('>>> v.dtype')
        coutln(v.dtype)
        # 1 dim array
        self.assertEqual(1, v.ndim)
        # shape = (10,)
        self.assertEqual(1, len(v.shape))
        self.assertEqual(10, v.shape[0])
        self.assertEqual(10, v.size)

        l: list = list(range(0, 10))
        self.assertTrue(np.array_equal(l, v))

    def test_linspace(self):
        """
        Learn numpy.linspace()

        python -m unittest tests.test_numpy.NumpyTest.test_linspace
        :return:
        """
        v: np.ndarray = np.linspace(0., 1000., 5)
        coutln('>>> np.linspace(0., 1000., 5)')
        coutln(v)
        coutln(v.dtype)

    def test_random(self):
        """
        python -m unittest tests.test_numpy.NumpyTest.test_random
        :return:
        """
        v: np.array = np.random.uniform(0., 1000., 5)
        coutln(v)

    def test_searchsorted(self):
        """
        python -m unittest tests.test_numpy.NumpyTest.test_searchsorted
        :return:
        """
        a: np.array = np.linspace(0., 1000., 9)
        coutln(a)
        v: np.array = np.random.uniform(0., 1000., 10)
        coutln(v)
        i: np.array = np.searchsorted(a, v)
        coutln(i)

    def test_record(self):
        """
        Learn numpy.record
        :return:
        """
        raise NotImplementedError

    def test_matrix(self):
        """
        python -m unittest tests.test_numpy.NumpyTest.test_matrix

        :return:
        """
        m = np.zeros((2,2))
        m[1,1] += 5.
        coutln(m)