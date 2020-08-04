import sys

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        widget = qtw.QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignVCenter)
        
        self.setCentralWidget(widget)
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
   
        
        
        