import sys

import PySide2.QtCore as qtc
import PySide2.QtGui as qtg
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        label = qtw.QLabel('Hello!')
        label.setAlignment(qtc.Qt.AlignCenter)
        
        toolbar = qtw.QToolBar('My main toolbar')
        toolbar.setIconSize(qtc.QSize(16,16))
        #toolbar.setToolButtonStyle(qtc.Qt.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)
        
        action = qtw.QAction(qtg.QIcon('fugue/icons/bug.png'), 'Your button', self)
        action.setStatusTip('This is your button')
        action.triggered.connect(self.onMyToolBarButtonClicked)
        action.setCheckable(True)
        toolbar.addAction(action)
        action.setShortcut(qtg.QKeySequence('Ctrl+p'))
        
        toolbar.addSeparator()
        
        action2 = qtw.QAction(qtg.QIcon('fugue/icons/bug.png'), 'Your button 2', self)
        action2.setStatusTip('This is your button 2')
        action2.triggered.connect(self.onMyToolBarButtonClicked)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        
        toolbar.addWidget(qtw.QLabel('Hello'))
        toolbar.addWidget(qtw.QCheckBox('Hello2'))
        
        status_bar = qtw.QStatusBar(self)
        self.setStatusBar(status_bar)
        
        
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu('Submenu')
        file_submenu.addAction(action2)
        
        self.setCentralWidget(label)
    def onMyToolBarButtonClicked(self, s):
        print('click', s)
        print('type: %s' % type(s))
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()