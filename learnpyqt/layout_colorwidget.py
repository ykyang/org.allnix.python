import PySide2.QtGui as qtg
import PySide2.QtWidgets as qtw

class Color(qtw.QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(qtg.QPalette.Window, qtg.QColor(color))
        self.setPalette(palette)