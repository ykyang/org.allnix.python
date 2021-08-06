# For qtpy used by qtawesome
import os
os.environ['QT_API'] = 'pyside2'
import qtawesome

## This must be before all other imports 
# Chapter 36
from PySide2 import QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

## Normal import stuff
from PySide2.QtCore import (
    QSize, 
    Qt,
    Slot,
)
from PySide2.QtGui import(
    #QIcon,
    QKeySequence,
    
)
from PySide2.QtWidgets import (
    QApplication,
    QAction,
    QCheckBox,
    QLabel,
    QMainWindow, QPushButton,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

def get_app():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow() #QWidget()
    window.show()
    app.exec_()
    #return app

# def hello3():
#     print("Hello3")

# Chapter 9 of Create GUI Application with Python and Qt5
class MainWindow9(QMainWindow):
    def __init__(me):
        super().__init__()
        me.setWindowIcon(qtawesome.icon('mdi.yin-yang'))
        me.setWindowTitle('Chapter 9')
        menu = me.menuBar()
        file_menu = menu.addMenu('&File')

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        me.setCentralWidget(label)

        toolbar = QToolBar('Main Toolbar')
        toolbar.setIconSize(QSize(32,32))
        me.addToolBar(toolbar)

        icon = qtawesome.icon('mdi.bug-outline')
        but = QAction(icon, 'Your button', me)
        but.setStatusTip('This is your button')
        but.setCheckable(True)
        but.setShortcut(QKeySequence('Ctrl+p'))
        but.triggered.connect(me.onMyToolBarButtonClick)
        toolbar.addAction(but)
        file_menu.addAction(but)

        toolbar.addSeparator()
        file_menu.addSeparator()

        icon = qtawesome.icon('mdi.atom')
        but = QAction(icon, 'But 2', me)
        but.setStatusTip('This is But 2')
        but.triggered.connect(me.onMyToolBarButtonClick)
        but.setCheckable(True)
        toolbar.addAction(but)
        
        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())
        file_menu.addAction(but)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(but)

        me.setStatusBar(QStatusBar(me))

        me.resize(400,300)
    def onMyToolBarButtonClick(me, checked):
        print('click', checked)


# https://stackoverflow.com/questions/58075822/pyside2-and-matplotlib-how-to-make-matplotlib-run-in-a-separate-process-as-i
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = fig = Figure(figsize=(7, 5), dpi=65, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        lay = QVBoxLayout(self)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

        # self.axes = fig.add_subplot(111)
        # self.line, *_ = self.axes.plot([])

    # @Slot(list)
    # def update_plot(self, data):
    #     self.line.set_data(range(len(data)), data)

    #     self.axes.set_xlim(0, len(data))
    #     self.axes.set_ylim(min(data), max(data))
    #     self.canvas.draw()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(me, parent=None, width=5, height=4, dpi=100):
        me.figure = figure =Figure(figsize=(width, height), dpi=dpi)
        #me.axes = figure.add_subplot(111)
        super().__init__(figure)

class MainWindow36(QMainWindow):
    def __init__(me):
        super().__init__()

        #sc = MplCanvas(me, width=5, height=4, dpi=100)
        sc = MatplotlibWidget(me)

        axes = sc.figure.add_subplot(111)
        axes.cla()
        me.plots = axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40],"r")
        sc.canvas.draw()
        # replot
        plot = me.plots[0]
        plot.set_ydata([1, 2,-1, 2, 3])


        me.setCentralWidget(sc)

        me.show()

