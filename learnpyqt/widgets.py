import sys

import PySide2.QtCore as qtc
import PySide2.QtGui as qtg
import PySide2.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
#         widget = qtw.QLabel('Hello')
#         font = widget.font()
#         font.setPointSize(30)
#         widget.setFont(font)
#         widget.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignVCenter)
        
#         widget.setPixmap(qtg.QPixmap('source/basic/otje.jpg'))
#         widget.setScaledContents(True)
        
#         widget = qtw.QCheckBox('This is a checkbox')
#         widget.setCheckState(qtc.Qt.Checked)
#         
#         # For tristate: widget.setCheckState(Qt.PartiallyChecked)         
#         #widget.setTriState(True)
#         widget.setTristate(True)
#         widget.stateChanged.connect(self.show_state)

#         widget = qtw.QComboBox()
#         widget.addItems(['One', 'Two', 'Three'])
#         widget.setEditable(True)
#         
#         widget.currentIndexChanged.connect(self.index_changed)
#         #print(type(widget.currentIndexChanged))
#         widget.currentTextChanged.connect(self.text_changed)                 
        
#         widget = qtw.QListWidget()
#         widget.addItems(['One', 'Two', 'Three'])
#         widget.currentItemChanged.connect(self.item_changed)
#         widget.currentTextChanged.connect(self.text_changed)
        
#         self.widget = widget = qtw.QLineEdit()
#         #widget.setMaxLength(10)
#         widget.setInputMask('(000)000-0000;_')
#         widget.setPlaceholderText("Enter your text")
#         
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)

#         widget = qtw.QSpinBox()
#         #widget = qtw.QDoubleSpinBox()
#         widget.setMinimum(-5)
#         widget.setMaximum(+5)
#         # widget.setRange
#         widget.setPrefix('$')
#         widget.setSuffix('c')
#         widget.setSingleStep(3)
#         widget.valueChanged.connect(self.value_changed)
#         widget.valueChanged[str].connect(self.value_changed_str)
                
        widget = qtw.QSlider(qtc.Qt.Horizontal)
        
        widget.setMinimum(-10)
        widget.setMaximum(3)
        
        widget.setSingleStep(3)
        
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
                
        
                
        self.setCentralWidget(widget)
    def slider_pressed(self):
        print('Pressed')
    
    def slider_released(self):
        print('Released')
        
    def slider_position(self, p):
        print('position = %i' % p)


    def value_changed(self, i):
        print('value = %i' % i)

    def value_changed_str(self, s):    
        print('value[str] = %s' % s)

    def return_pressed(self):
        print('Return pressed')
        self.widget.setText('BOOM!')
        
    def selection_changed(self):
        print('Selection changed')
        print(self.widget.selectedText())
        
    def text_changed(self, s):
        print('Text changed...')
        print(s)
        
    def text_edited(self, s):
        print('Text edited...')
        print(s)
        
    def item_changed(self, item):
        print(item.text())
        
    def index_changed(self, i):
        print(i)
        
        
#     def text_changed(self, s):
#         print(s)
        
    def show_state(self, s):
        print(s == qtc.Qt.Checked)
        print(s)
        
        
app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
   
        
        
        