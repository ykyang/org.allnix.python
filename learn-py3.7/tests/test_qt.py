import unittest

import sys

from allnix.qt.learn import MyWidget, MyForm, MyCommunicate, MyMainWindow
from allnix.qt.learn import MyThemeWidget
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCharts import QtCharts


class QtTest(unittest.TestCase):
    def test_MyWidget(self) -> None:
        """
        python -m unittest tests.test_qt.QtTest.test_MyWidget
        :return:
        """
        app = QApplication(sys.argv)
        widget = MyWidget()
        widget.resize(400, 300)
        widget.show()
        app.exec_()

    def test_MyForm(self):
        """
        python -m unittest tests.test_qt.QtTest.test_MyForm
        :return:
        """
        app = QApplication(sys.argv)
        form = MyForm()
        form.show()
        app.exec_()

    def test_MyCommunication(self):
        """
        python -m unittest tests.test_qt.QtTest.test_MyCommunication
        :return:
        """
        someone = MyCommunicate()

        someone.signal_number.connect(someone.say_something)
        someone.signal_word.connect(someone.say_something)

        someone.signal_number.emit(10)
        someone.signal_word.emit('Hello everybody!')

        someone.signal_multiplex.connect(someone.say_something) # (int,)
        someone.signal_multiplex[str].connect(someone.say_something) # (str,)

        someone.signal_multiplex.emit(10)
        someone.signal_multiplex[str].emit("Hello from multiplex!")

    def test_BarChart(self):
        """
        python -m unittest tests.test_qt.QtTest.test_BarChart
        :return:
        """
        app = QApplication(sys.argv)
        w = MyMainWindow()
        w.resize(420, 300)
        w.show()
        app.exec_()

    def test_ThemeWidget(self):
        """
        python -m unittest tests.test_qt.QtTest.test_ThemeWidget
        :return:
        """
        app = QApplication(sys.argv)
        window = QMainWindow()
        widget = MyThemeWidget(None)
        window.setCentralWidget(widget)
        available_geometry = app.desktop().availableGeometry(window)
        size = available_geometry.height() * 0.75
        window.setFixedSize(size, size * 0.8)
        window.show()
        app.exec_()