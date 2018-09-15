import unittest

import sys

from allnix.qt.learn import MyWidget, MyForm, MyCommunicate
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