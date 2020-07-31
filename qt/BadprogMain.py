# badprog.com

import sys


#

from PySide2.QtWidgets  import QApplication, QMainWindow

from BadprogWindow      import Ui_MainWindow


#

class MainWindow(QMainWindow, Ui_MainWindow):

    #

    def __init__(self):

        #

        QMainWindow.__init__(self)


        #

        self.setupUi(self)

        self.connectMe()


        #

        self.setWindowTitle("Hello World from Badprog :D")

        self.setFixedWidth(500)

        self.setFixedHeight(500)


    #

    def connectMe(self):

        self.pushButton.clicked.connect(self.slotButton)

 

    #

    def slotButton(self):

        self.label.setText("Hello from Badprog :D ")

 

#

if (__name__ == '__main__'):

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()

    sys.exit(app.exec_())