import unittest
import sys

import numpy as np
import pandas as pd

class PandasTest(unittest.TestCase):
    _cout = sys.stdout
    _cerr = sys.stderr

    def cout(self, value):
        self._cout.write('{}'.format(value))

    def coutln(self, value=None):
        if value is None:
            self._cout.write('\n')
        else:
            self._cout.write('{}\n'.format(value))

    def cerr(self, value):
        self._cerr.write('{}\n'.format(value))

    _df = None
    _df2 = None

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

    def test_10_minutes_to_pandas(self):
        """
        http://pandas.pydata.org/pandas-docs/stable/10min.html

        To run the test:
        python -m unittest tests.test_pandas.PandasTest.test_object_creation

        :return:
        """
        # Template
        # self.cout("\n>>> \n{}\n".format())

        # >
        # > Object Creation
        # >

        # Creating a Series by passing a list of values,
        # letting pandas create a default integer index:
        s = pd.Series([1,3,5,np.nan,6,8])
        self.coutln(s)

        # Creating a DataFrame by passing a NumPy array,
        # with a datetime index and labeled columns:
        dates = pd.date_range('2018-09-06', periods = 6)
        self.coutln('\ndates:')
        self.coutln(dates)
        self.cout('type(dates): {}\n'.format(type(dates)))

        df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
        self.cout('\ndf:\n{}\n'.format(df))

        # DataFrame from dictionary
        df2 = pd.DataFrame(
            {
                'A': 1.,
                'B': pd.Timestamp('2013-01-02'),
                'C': pd.Series(1, index = list(range(4)), dtype='float32'),
                'D': np.array([3]*4, dtype='int32'),
                'E': pd.Categorical(['test','train', 'test', 'train']),
                'F': 'foo'
            }
        )
        self.coutln('\n>>> df2\n{}\n'.format(df2))

        self.cout('\n>>> df2.dtypes\n{}\n'.format(df2.dtypes))

        # >
        # > Viewing Data
        # >
        self.cout('\n>>> df.head()\n{}\n'.format(df.head()))
        self.cout('\n>>> df.head(2)\n{}\n'.format(df.head(2)))
        self.cout('\n>>> df.tail(3)\n{}\n'.format(df.tail(3)))
        self.cout('\n>>> df.index\n{}\n'.format(df.index))
        self.cout('\n>>> df.columns\n{}\n'.format(df.columns))
        self.cout('\n>>> type(df.columns)\n{}\n'.format(type(df.columns)))
        self.cout('\n>>> df.values\n{}\n'.format(df.values))
        self.cout('\n>>> df.describe()\n{}\n'.format(df.describe()))

        tdf = df.T
        self.cout('\n>>> df.T\n{}\n'.format(tdf))

        tdf = df.sort_index(axis=0, ascending=False)
        self.cout('\n>>> df.sort_index(axis=0, ascending=False)\n{}\n'.format(tdf))

        tdf = df.sort_index(axis=1, ascending=False)
        self.cout('\n>>> df.sort_index(axis=1, ascending=False)\n{}\n'.format(tdf))

        tdf = df.sort_values(by='B')
        self.cout("\n>>> df.sort_values(by='B')\n{}\n".format(tdf))

        #>
        #> Selection
        #>

        #>
        #> Selection by Label
        #>
        ts = df['A']
        self.cout("\n>>> df['A']\n{}\n".format(ts))

        # Selecting via [], which slices the rows.
        tdf = df[0:3]
        self.cout('\n>>> df[0:3]\n{}\n'.format(tdf))

        #> loc
        #> https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html

        ts = df.loc[dates[0]]
        self.cout('\n>>> df.loc[dates[0]]\n{}\n'.format(ts))

        tdf = df.loc[:,['A','B']]
        self.cout("\n>>> df.loc[:,['A','B']]\n{}\n".format(tdf))

        tdf = df.loc['2018-09-07':'2018-09-10', ['A','B']]
        self.cout("\n>>> df.loc['2018-09-07':'2018-09-10', ['A','B']]\n{}\n".format(tdf))

        ts = df.loc['2018-09-08',['A', 'B']]
        self.cout("\n>>> df.loc['2018-09-08',['A', 'B']]\n{}\n".format(ts))

        # For getting a scalar value:
        v = df.loc[dates[0], 'A']
        self.cout("\n>>> df.loc[dates[0], 'A']\n{}\n".format(v))
        # For getting fast access to a scalar (equivalent to the prior method):
        v = df.at[dates[0], 'A']
        self.cout("\n>>> df.at[dates[0], 'A']\n{}\n".format(v))

        #>
        #> Selection by Position
        #>