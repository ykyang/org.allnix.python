import sys
import random
import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

window_titles = ['My App' ,
                 'My App' ,
                 'Still My App',
                 'Still My App' ,     'What on earth' ,     'What on earth' ,     
                 'This is surprising',     
                 'This is surprising',     
                 'Something went wrong']

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        #self.button_is_checked = True
        self.n_times_clicked = 0
        
        self.setWindowTitle('My App')
        
        self.button = button = qtw.QPushButton('Press Me!')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        #button.clicked.connect(self.the_button_was_toggled)
        #button.released.connect(self.the_button_was_released)
        
        #button.setChecked(self.button_is_checked)
 
        self.setFixedSize(400,300)
        # Try
        # self.setMinimumSize()
        # self.setMaximimSize()
        
        self.setCentralWidget(button)
            
    def the_button_was_clicked(self):
        #self.button.setText('You already clicked me.')
        #self.button.setEnabled(False)
        new_window_title = random.choice(window_titles)
        self.setWindowTitle(new_window_title)
        
    def the_window_title_changed(self, window_title):
        print('Window title changed: %s' % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(checked)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

