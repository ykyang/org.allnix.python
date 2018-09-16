import sys
import random

from PySide2.QtCore import Qt, QObject, Signal, Slot
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtWidgets import QDialog, QLineEdit, QMainWindow
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter

class MyWidget(QWidget):
    """
    http://blog.qt.io/blog/2018/05/04/hello-qt-for-python/
    """
    layout: QVBoxLayout
    text: QLabel
    hello: list
    button: QPushButton

    def __init__(self):
        QWidget.__init__(self)

        self.hello = ['Hallo welt!', 'Ciao mondo!', 'Hei maailma!', 'Hola mundo!',
                      'Hei verden!', '你好，世界', 'Привет мир']

        self.button= QPushButton('Click me!')
        self.text = QLabel('Hello World')
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic)

        #print(type(self.button.clicked))

    def magic(self):
        self.text.setText(random.choice(self.hello))

class MyForm(QDialog):
    """
    https://wiki.qt.io/Qt_for_Python_Tutorial_SimpleDialog
    """
    button: QPushButton
    edit: QLineEdit

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit('Write my name here')
        self.button = QPushButton('Show Greetings')
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print('Hello {}'.format(self.edit.text()))

class MyCommunicate(QObject):
    """
    https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    """
    signal_number = Signal(int)
    signal_word = Signal(str)
    signal_multiplex = Signal((int,), (str,))



    @Slot(int)
    @Slot(str)
    def say_something(self, words):
        print(words)


class MyMainWindow(QMainWindow):
    """
    miniconda3/envs/py37/lib/python3.7/site-packages/
    PySide2/examples/charts/percentbarchart.py
    """
    def __init__(self):
        QMainWindow.__init__(self)

        set0 = QtCharts.QBarSet("Jane")
        set1 = QtCharts.QBarSet("John")
        set2 = QtCharts.QBarSet("Axel")
        set3 = QtCharts.QBarSet("Mary")
        set4 = QtCharts.QBarSet("Samantha")

        set0.append([1, 2, 3,  4, 5, 6])
        set1.append([5, 0, 0,  4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7,  3, 4, 5])
        set4.append([9, 7, 5,  3, 1, 2])

        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Simple percentbarchart example")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)
