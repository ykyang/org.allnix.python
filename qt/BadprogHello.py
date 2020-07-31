# https://www.badprog.com/python-3-pyside2-setting-up-and-using-qt-designer
# badprog.com

import sys


#

from PySide2.QtWidgets  import QApplication, QMainWindow


#

class MainWindow(QMainWindow):

    #

    def __init__(self):

        #

        QMainWindow.__init__(self)

        self.setWindowTitle("Hello World from Badprog :D")

        self.setFixedWidth(500)

        self.setFixedHeight(500)

 

#

if (__name__ == '__main__'):

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()

    sys.exit(app.exec_())