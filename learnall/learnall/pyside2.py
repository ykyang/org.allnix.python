from PySide2.QtCore import (
    QSize, Qt,
    
)
from PySide2.QtWidgets import (
    QApplication,
    QAction,
    QLabel,
    QMainWindow, QPushButton,
    QToolBar,
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

        me.setWindowTitle('Chapter 9')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        me.setCentralWidget(label)

        toolbar = QToolBar('Main Toolbar')
        me.addToolBar(toolbar)

        but = QAction('Your button', me)
        but.setStatusTip('This is your button')
        but.triggered.connect(me.onMyToolBarButtonClick)
        toolbar.addAction(but)

        me.resize(400,300)
    def onMyToolBarButtonClick(me, s):
        print('click', s)