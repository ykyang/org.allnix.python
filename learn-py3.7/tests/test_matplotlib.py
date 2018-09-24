import unittest

from tests import coutln

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

class MatplotlibTest(unittest.TestCase):
    def test_scatter_demo2(self):
        """

        https://matplotlib.org/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py

        python -m unittest tests.test_matplotlib.MatplotlibTest.test_scatter_demo2
        :return:
        """

        with cbook.get_sample_data('goog.npz') as datafile:
            # coutln(datafile)
            data:np.lib.npyio.NpzFile = np.load(datafile)
            price_data: np.recarray = data['price_data'].view(np.recarray)
            # coutln('>>> price_data')
            # coutln(price_data)
            coutln('>>> type(price_data)')
            coutln(type(price_data))
            coutln('>>> price_data.dtype')
            coutln(price_data.dtype)
            # coutln(price_data.view(np.recarray))
            # coutln('>>> price_data.size')
            # coutln(price_data.size)
            # for i in data.keys():
            #     coutln(i)

            price_data = price_data[-250:]
            # coutln('>>> price_data')
            # coutln(price_data)

            coutln(">>> price_data.adj_close.size")
            coutln(price_data.adj_close.size)

            # price_data.adj_close[:-1]: first to second to the last
            delta1: np.ndarray = np.diff(price_data.adj_close) / price_data.adj_close[:-1]
            coutln(">>> delta1.size")
            coutln(delta1.size)

            volume = (15 * price_data.volume[:-2]/price_data.volume[0])**2
            coutln('volume.size: {}'.format(volume.size))
            close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

            fig: matplotlib.figure.Figure
            ax: matplotlib.axes.Axes
            fig, ax = plt.subplots()
            ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

            ax.set_xlabel(r'$\Delta_i$', fontsize=15)
            ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
            ax.set_title('Volume and percent change')

            ax.grid(True)
            fig.tight_layout()

            plt.show()