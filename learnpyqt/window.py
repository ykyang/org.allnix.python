import sys
import random
import PySide2.QtWidgets as qtw

class AnotherWindow(qtw.QWidget):
    """
    This 'window' is a QWidget
    """
    def __init__(self):
        super().__init__()
        id = random.randint(1,100)
        layout = qtw.QVBoxLayout()
        label = qtw.QLabel('Another Window: {}'.format(id))
        layout.addWidget(label)
        
        self.setLayout(layout)
        
    
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.w = AnotherWindow()
        
        button = self.button = qtw.QPushButton('Push for Window')
#         button.clicked.connect(self.show_new_window)
        button.clicked.connect(self.toggle_window)
        self.setCentralWidget(button)
        
    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        
    def show_new_window(self, checked):
        self.w.show()
        
#     def show_new_window(self, checked):
#         if self.w is None:
#             self.w = AnotherWindow()
#             self.w.show()
#         else:
#             self.w = None

app = qtw.QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec_()


        