import sys
import random

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# app = QApplication([])
# label = QLabel('Hello Qt for Python!')
# label.show()
# app.exec_()

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
                      'Hei verden!']

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec_())

