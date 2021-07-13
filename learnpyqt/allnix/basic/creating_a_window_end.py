import sys
import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        button = qtw.QPushButton('Press Me!')
 
        self.setFixedSize(400,300)
        # Try
        # self.setMinimumSize()
        # self.setMaximimSize()
        
        self.setCentralWidget(button)
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

