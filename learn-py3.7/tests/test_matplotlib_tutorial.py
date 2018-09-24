import unittest

from tests import coutln

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class MatplotlibTest(unittest.TestCase):
    """
    https://www.labri.fr/perso/nrougier/teaching/matplotlib/
    """
    def test_simple_plot(self):
        """
        python -m unittest tests.test_matplotlib_tutorial.MatplotlibTest.test_simple_plot
        :return:
        """
        params = mpl.rcParams

        fig: mpl.figure.Figure = plt.figure(figsize=(8,6), dpi=100)
        axs: mpl.axes.Axes = plt.subplot(1,1,1)

        x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        c = np.cos(x)
        s = np.sin(x)

        axs.plot(x, s, color='green', linewidth=1.5, linestyle='-', label='sin')
        axs.plot(x, c, color='blue', linewidth=1.5, linestyle='-', label='cos')
        axs.legend(loc='upper left', frameon=True)

        axs.set_xlim(-4.0, 4.0)
        # axs.set_xticks(np.linspace(-4, 4, 9, endpoint=True))
        axs.set_ylim(-1.1, 1.1)
        # axs.set_yticks(np.linspace(-1, 1, 5, endpoint=True))

        axs.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
        axs.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
        # plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
        #                [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

        # axs.set_yticks([-1, 0, 1])
        # axs.set_yticklabels([r'$-1$', r'$0$', r'$+1$'])
        axs.set_yticks([-1, 1])
        axs.set_yticklabels([r'$-1$', r'$+1$'])

        # ax = plt.gca()
        # coutln(type(ax))

        # > How in the hell would I know this?
        axs.spines['right'].set_color('none')
        axs.spines['top'].set_color('none')
        axs.xaxis.set_ticks_position('bottom')
        axs.spines['bottom'].set_position(('data', 0))
        axs.yaxis.set_ticks_position('left')
        axs.spines['left'].set_position(('data', 0))

        t = 2*np.pi/3
        axs.plot([t,t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle='--')
        axs.scatter([t,],[np.cos(t),], 50, color='blue')
        axs.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

        axs.plot([t, t], [0, np.sin(t)], color='red', linewidth=1.5, linestyle="--")
        axs.scatter([t, ], [np.sin(t), ], 50, color='red')

        axs.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                     xy=(t, np.cos(t)), xycoords='data',
                     xytext=(-90, -50), textcoords='offset points', fontsize=16,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

        for label in axs.get_xticklabels() + axs.get_yticklabels():
            label.set_fontsize(16)
            label.set_bbox(dict(facecolor='yellow', zorder=3, fill=True, alpha=0.5))

        # > Save to file
        # fig.savefig('exercise_2.png', dpi=100)
        plt.show()