import unittest
import sys

from tests import *

import numpy as np
import pandas as pd

class PandasTest(unittest.TestCase):
    # _cout = sys.stdout
    # _cerr = sys.stderr
    #
    # def cout(self, value):
    #     self._cout.write('{}'.format(value))
    #
    # def coutln(self, value=None):
    #     if value is None:
    #         self._cout.write('\n')
    #     else:
    #         self._cout.write('{}\n'.format(value))
    #
    # def cerr(self, value):
    #     self._cerr.write('{}\n'.format(value))

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
        python -m unittest tests.test_pandas.PandasTest.test_10_minutes_to_pandas

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
        coutln(s)

        # Creating a DataFrame by passing a NumPy array,
        # with a datetime index and labeled columns:
        dates = pd.date_range('2018-09-06', periods = 6)
        coutln('\ndates:')
        coutln(dates)
        cout('type(dates): {}\n'.format(type(dates)))

        df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
        cout('\ndf:\n{}\n'.format(df))

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
        coutln('\n>>> df2\n{}\n'.format(df2))

        cout('\n>>> df2.dtypes\n{}\n'.format(df2.dtypes))

        # >
        # > Viewing Data
        # >
        cout('\n>>> df.head()\n{}\n'.format(df.head()))
        cout('\n>>> df.head(2)\n{}\n'.format(df.head(2)))
        cout('\n>>> df.tail(3)\n{}\n'.format(df.tail(3)))
        cout('\n>>> df.index\n{}\n'.format(df.index))
        cout('\n>>> df.columns\n{}\n'.format(df.columns))
        cout('\n>>> type(df.columns)\n{}\n'.format(type(df.columns)))
        cout('\n>>> df.values\n{}\n'.format(df.values))
        cout('\n>>> df.describe()\n{}\n'.format(df.describe()))

        tdf = df.T
        cout('\n>>> df.T\n{}\n'.format(tdf))

        tdf = df.sort_index(axis=0, ascending=False)
        cout('\n>>> df.sort_index(axis=0, ascending=False)\n{}\n'.format(tdf))

        tdf = df.sort_index(axis=1, ascending=False)
        cout('\n>>> df.sort_index(axis=1, ascending=False)\n{}\n'.format(tdf))

        tdf = df.sort_values(by='B')
        cout("\n>>> df.sort_values(by='B')\n{}\n".format(tdf))

        #>
        #> Selection
        #>

        #>
        #> Selection by Label
        #>
        ts = df['A']
        cout("\n>>> df['A']\n{}\n".format(ts))

        # Selecting via [], which slices the rows.
        tdf = df[0:3]
        cout('\n>>> df[0:3]\n{}\n'.format(tdf))

        #> loc
        #> https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.loc.html

        ts = df.loc[dates[0]]
        cout('\n>>> df.loc[dates[0]]\n{}\n'.format(ts))

        tdf = df.loc[:,['A','B']]
        cout("\n>>> df.loc[:,['A','B']]\n{}\n".format(tdf))

        tdf = df.loc['2018-09-07':'2018-09-10', ['A','B']]
        cout("\n>>> df.loc['2018-09-07':'2018-09-10', ['A','B']]\n{}\n".format(tdf))

        ts = df.loc['2018-09-08',['A', 'B']]
        cout("\n>>> df.loc['2018-09-08',['A', 'B']]\n{}\n".format(ts))

        # For getting a scalar value:
        v = df.loc[dates[0], 'A']
        cout("\n>>> df.loc[dates[0], 'A']\n{}\n".format(v))
        # For getting fast access to a scalar (equivalent to the prior method):
        v = df.at[dates[0], 'A']
        cout("\n>>> df.at[dates[0], 'A']\n{}\n".format(v))

        #>
        #> Selection by Position
        #>
        cout("\n>>> df\n{}\n".format(df))

        ts = df.iloc[3]
        cout("\n>>> df.iloc[3]\n{}\n".format(ts))

        tdf = df.iloc[3:5, 0:2]
        cout("\n>>> df.iloc[3:5, 0:2]\n{}\n".format(tdf))

        tdf = df.iloc[[1,2,4],[0,2]]
        cout("\n>>> df.iloc[[1,2,4],[0,2]]\n{}\n".format(tdf))

        # For slicing rows explicitly:
        tdf = df.iloc[1:3,:]
        cout("\n>>> df.iloc[1:3,:]\n{}\n".format(tdf))

        #For slicing columns explicitly:
        tdf = df.iloc[:,1:3]
        cout("\n>>> df.iloc[:,1:3]\n{}\n".format(tdf))

        # For getting a value explicitly:
        v = df.iloc[1,1]
        cout("\n>>> df.iloc[1,1]\n{}\n".format(v))

        # For getting fast access to a scalar (equivalent to the prior method):
        v = df.iat[1,1]
        cout("\n>>> df.iat[1,1]\n{}\n".format(v))

        #>
        #> Boolean Indexing
        #>
        cout("\n>>> df\n{}\n".format(df))

        tdf = df[df['A'] > 0]
        cout("\n>>> df[df['A'] > 0]\n{}\n".format(tdf))

        tdf = df[df > 0]
        cout("\n>>> df[df > 0]\n{}\n".format(tdf))

        # Using the isin() method for filtering:
        df2 = df.copy()
        df2['E'] = ['one', 'one','two','three','four','three']
        cout("\n>>> df2\n{}\n".format(df2))

        tdf = df2[df2['E'].isin(['two', 'four'])]
        cout("\n>>> df2[df2['E'].isin(['two', 'four'])]\n{}\n".format(tdf))

        #>
        #> Setting
        #>
        cout("\n>>> df\n{}\n".format(df))

        # Setting a new column automatically aligns the data by the indexes.
        # notice the index range is out of bound at the end
        ts = pd.Series(data=[1,2,3,4,5,6],
                       index=pd.date_range('2018-09-07', periods=6))
        cout("\n>>> A series with out of bound index\n{}\n".format(ts))
        df['F'] = ts
        cout("\n>>> df\n{}\n".format(df))
        cout('\nNotice the NaN at the top and missing 6.0 at the end of column F\n')

        # A where operation with setting.
        df2 = df.copy()
        df2[df2 > 0] = -df2
        cout("\n>>> df2[df2 > 0] = -df2\n{}\n".format(df2))
        cout('\nAll the positive numbers are now negative\n')

        # >
        # > Missing Data
        # >
        cout('\n'*10)
        coutln('--------------------')
        coutln('--- missing data ---')
        coutln('--------------------')
        coutln("\n>>> df\n{}".format(df))
        df1 = df.reindex(index=dates[0:4], columns=list(df.columns).append('E'))
        cout("\n>>> df1: Reindexed but no data\n{}\n".format(df1))
        df1.loc[dates[0]:dates[1],'E'] = 1
        cout("\n>>> df1: 'E' column data set\n{}\n".format(df1))

        # To drop any rows that have missing data.
        df2 = df1.dropna(how='any')
        cout("\n>>> df1.dropna(how='any')\n{}\n".format(df2))

        # Filling missing data.
        df2 = df1.fillna(value=5)
        cout("\n>>> df1.fillna(value=5)\n{}\n".format(df2))

        # To get the boolean mask where values are nan.
        df2 = pd.isna(df1)
        cout("\n>>> pd.isna(df1)\n{}\n".format(df2))

        # > My own NaN test
        coutln("\n>>> df\n{}".format(df))
        ts = df.loc[:, 'F']
        coutln("\n>>> ts = df.loc[:, 'F']\n{}".format(ts))
        self.assertEqual(6, ts.size)
        self.assertTrue(pd.isnull(ts[0]))
        # > strip NaN
        ts = ts[pd.notnull(ts)]
        coutln("\n>>> ts = ts[pd.notnull(ts)]\n{}".format(ts))
        self.assertEqual(5, ts.size)
        self.assertEqual(1.0, ts[0])
        self.assertEqual(5.0, ts[4])

        # >
        # > Operations
        # >

        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())
        # cout("\n>>> \n{}\n".format())