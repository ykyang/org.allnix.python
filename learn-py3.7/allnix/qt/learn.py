import sys
import random

from PySide2.QtCore import Qt, QObject, Signal, Slot
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PySide2.QtWidgets import QDialog, QLineEdit

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
    signal_number = Signal(int)
    signal_word = Signal(str)
    signal_multiplex = Signal((int,), (str,))



    @Slot(int)
    @Slot(str)
    def say_something(self, words):
        print(words)



