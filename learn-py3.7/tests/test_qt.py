import unittest

import sys

from allnix.qt.learn import MyWidget, MyForm
from PySide2.QtWidgets import QApplication

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