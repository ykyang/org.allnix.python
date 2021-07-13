import sys
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        label = self.label = qtw.QLabel('Click in this window')
        
        self.setMouseTracking(True) # does not work? 
        
        self.setCentralWidget(label)
        
    def mouseMoveEvent(self, e):
        """Callback function when mouse moved
        
        Mouse must be clicked while moving to trigger this function.
        
        Keyword arguments:
        e -- event
        """
        
        self.label.setText('mouseMoveEvent')
        
    def mousePressEvent(self, e):
        self.label.setText('mousePressEvent')
        
    def mouseReleaseEvent(self, e):
        self.label.setText('mouseReleaseEvent')
        
    def mouseDoubleClickEvent(self, e):
        self.label.setText('mouseDoubleClickEvent')
        
app = qtw.QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec_()

