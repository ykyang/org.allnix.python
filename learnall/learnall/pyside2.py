from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
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