import unittest

import numpy as np
import pandas as pd

class PandasTest(unittest.TestCase):
    """
    http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
    """
    def test_series(self):
        s = pd.Series(np.random.randn(5),index=['a', 'b', 'c', 'd', 'e'])
        print('s = \n{}\n'.format(s))
        print(s.index)

        s = pd.Series(np.random.randn(5))
        print('s = \n{}\n'.format(s))

        d = {'b' : 1, 'a' : 0, 'c' : 2}
        s = pd.Series(d)
        print('s = \n{}\n'.format(s))

        s = pd.Series(d, index=['b', 'c', 'd', 'a'])
        print('s = \n{}\n'.format(s))

        s = pd.Series(5.0, index=['a', 'b', 'c', 'd', 'e'])
        print("pd.Series(5.0, index=['a', 'b', 'c', 'd', 'e']) -> \n{}\n".format(s))

        s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
        print('s = \n{}\n'.format(s))
        print('s[0] = \n{}\n'.format(s[0]))
        print('s[:3] = \n{}\n'.format(s[:3]))
        print('s[s>s.median()]\n{}\n'.format(s[s>s.median()]))

        print([s > s.median()])
        print(s[[True, False, False, True, True]])

    def test_dataframe(self):
        """
        python -m unittest tests.test_pandas.PandasTest.test_dataframe

        :return:
        """
        d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
             'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

        df = pd.DataFrame(d)

        print(df)

        df = pd.DataFrame(df, index=['d', 'b', 'a'])
        print(df)

        df = pd.DataFrame(df, index=['d', 'b', 'a'], columns=['two', 'one'])
        print(df)

        data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
        data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
        df = pd.DataFrame(data)
        print(df)

        # Column selection, addition, deletion¶