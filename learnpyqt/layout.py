import sys

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from layout_colorwidget import Color

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        #layout = qtw.QVBoxLayout()
        
#         layout = qtw.QHBoxLayout()
#         # Nested layout
#         # W: ABC
#         # W.A: VBox
#         # W.B: widget
#         # W.C: VBox
#         W = qtw.QHBoxLayout()
#         A = qtw.QVBoxLayout()
#         B = Color('green')
#         C = qtw.QVBoxLayout()
#         
#         A.addWidget(Color('red'))
#         A.addWidget(Color('yellow'))
#         A.addWidget(Color('purple'))
#         
#         C.addWidget(Color('red'))
#         C.addWidget(Color('purple'))
#         
#         W.addLayout(A)
#         W.addWidget(B)
#         W.addLayout(C)
#         
#         W.setContentsMargins(5, 10, 15, 20)
#         W.setSpacing(1)

                
#         W = layout = qtw.QGridLayout()
#         layout.addWidget(Color('red'), 0, 0)
#         layout.addWidget(Color('green'), 1, 0)
#         layout.addWidget(Color('blue'), 1, 1)
#         layout.addWidget(Color('purple'), 2, 1)
                
        
#         W = layout = qtw.QStackedLayout()
#         
#         red = Color('red')
#         
#         layout.addWidget(red)
#         layout.addWidget(Color('green'))
#         layout.addWidget(Color('blue'))
#         layout.addWidget(Color('yellow'))
#         
#         # 2 ways to set 
#         layout.setCurrentWidget(red) # red
#         #layout.setCurrentIndex(3) # yellow
        
        
#         # W:
#         # AAAA
#         # BBBB
#         # BBBB
#         #
#         # W: main widget
#         # W.A: buttons
#         # W.B: display area
#         
#         W = page_layout = qtw.QVBoxLayout()
#         A = button_layout = qtw.QHBoxLayout()
#         B = self.stack_layout = qtw.QStackedLayout()
#         
#         W.addLayout(A)
#         W.addLayout(B)
#         
#         btn = qtw.QPushButton('Red')
#         btn.clicked.connect(lambda: self.activate_tab(0))
#         A.addWidget(btn)
#         B.addWidget(Color('red'))
#         
#         btn = qtw.QPushButton('Green')
#         btn.clicked.connect(lambda: self.activate_tab(1))
#         A.addWidget(btn)
#         B.addWidget(Color('green'))
#         
#         btn = qtw.QPushButton('Blue')
#         btn.clicked.connect(lambda: self.activate_tab(2))
#         A.addWidget(btn)
#         B.addWidget(Color('blue'))
#         
#         btn = qtw.QPushButton('Yellow')
#         btn.clicked.connect(lambda: self.activate_tab(3))
#         A.addWidget(btn)
#         B.addWidget(Color('yellow'))
#         
#         B.setCurrentIndex(0)
#         
#         widget = qtw.QWidget()
#         widget.setLayout(W)
        
        widget = tabs = qtw.QTabWidget()
        tabs.setTabPosition(tabs.West)
        tabs.setMovable(True)
        
        for ind,color in enumerate(['red', 'green', 'blue', 'yellow']):
            tabs.addTab(Color(color), color)
            
            
        
        
        
        self.setCentralWidget(widget)
        
    def activate_tab(self, ind):
        self.stack_layout.setCurrentIndex(ind)
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
