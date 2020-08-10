import sys
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        button = qtw.QPushButton('Press me for a dialog!')
        button.clicked.connect(self.button_clicked)
        
        self.setCentralWidget(button)
        
        
    def button_clicked(self, s):
        print('click: {} {}'.format(s, type(s)))
        
#         dlg = qtw.QDialog(self)
#         dlg.setWindowTitle('Hello!')
#         dlg.exec_()


#         dlg = CustomDialog()
#         ans = dlg.exec_()
#         if ans:
#             print('Success!')
#         else:
#             print('Cancel!')
        
        
#         dlg = qtw.QMessageBox(self)    
#         dlg.setWindowTitle('I have a question!')        
#         dlg.setText('This is a simple dialog')
#         dlg.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No)
#         dlg.setIcon(qtw.QMessageBox.Question)
#         ans = dlg.exec_()
#         print('ans type: {}'.format(type(ans)))
#         
#         if ans == qtw.QMessageBox.Ok:
#             print('OK!')
#         elif ans == qtw.QMessageBox.Yes:
#             print('YES!')
         
        ans = qtw.QMessageBox.question(self, 'Question dialog', 'The longer message')
        print('type of ans: {}'.format(type(ans)))
        if ans == qtw.QMessageBox.Yes:
            print('YES!')
        else:
            print('NO!')

        
class CustomDialog(qtw.QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Hello!')
        
        QBtn = qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel
        
        bbox = self.buttonBox = qtw.QDialogButtonBox(QBtn)
        bbox.accepted.connect(self.accept) # self.accept is a base
        bbox.rejected.connect(self.reject)
        
        layout = self.layout = qtw.QVBoxLayout()
        message = qtw.QLabel('Something happened, is that OK?')
        layout.addWidget(message)
        layout.addWidget(bbox)
        self.setLayout(layout)
        
        
    
    
app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()