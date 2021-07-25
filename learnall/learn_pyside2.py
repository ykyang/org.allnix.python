def hello():
    # 
    # https://en.wikipedia.org/wiki/PySide
    #
    import sys
    from PySide2 import QtCore, QtWidgets

    # Create a Qt application
    app = QtWidgets.QApplication(sys.argv)

    # Create a Window
    mywindow = QtWidgets.QWidget()
    mywindow.resize(320, 240)
    mywindow.setWindowTitle('Hello, World!')

    # Create a label and display it all together
    mylabel = QtWidgets.QLabel(mywindow)
    mylabel.setText('Hello, World!')
    mylabel.setGeometry(QtCore.QRect(200, 200, 200, 200))

    mywindow.show()

    # Enter Qt application main loop
    sys.exit(app.exec_())


# https://www.pythonguis.com/courses/pyside-getting-started/


def learn_first_app_with_pyside():
    """https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
    """
    from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow() #QWidget()
    window.setFixedSize(QSize(400,300))
    window.show()
    app.exec_()

#learn_first_app_with_pyside()

from PySide2 import QtCore
from PySide2.QtCore import QSize, QTimer, QRunnable, QThreadPool
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide2.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QMenu, QAction
from random import choice
import time
import threading

import learnall.pyside2

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.n_times_clicked = 0
        # self.button_is_checked = True

        self.setWindowTitle("My App")
        
        label = self.label = QLabel()
        input = self.input = QLineEdit()
        input.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        layout.addWidget(input)
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # button = self.button = QPushButton("Press Me!")
        # button.clicked.connect(self.the_button_was_clicked)
        # self.windowTitleChanged.connect(self.the_window_title_changed)
        #button.setCheckable(True)
        #button.clicked.connect(self.the_button_was_clicked)
        #button.clicked.connect(self.the_button_was_toggled)
        #button.released.connect(self.the_button_was_released)
        #button.setChecked(self.button_is_checked)
        #self.setFixedSize(QSize(400,300))
        
        #self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Clicked!')
        new_window_title = choice(window_titles)
        print('Setting title: %s' % new_window_title)

        # self.button.setText('You already clicked me!')
        # self.button.setEnabled(False)
        self.setWindowTitle(new_window_title)
    def the_window_title_changed(self, window_title):
        print('Window title changed: {}'.format(window_title))
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", checked)
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

class MainWindow2(QMainWindow):
    """https://www.pythonguis.com/tutorials/pyside-signals-slots-events/
    """
    def __init__(me):
        super().__init__()
        me.label = QLabel('Click in this window')
        me.setCentralWidget(me.label)
        me.setMouseTracking(True)

    def mouseMoveEvent(me, event):
        me.label.setText('mouseMoveEvent')
    def mousePressEvent(me, event):
        me.label.setText('mousePressEvent')
        #super(MainWindow2, me).contextMenuEvent(event)
    def mouseReleaseEvent(me, event):
        me.label.setText('mouseReleaseEvent')
    def mouseDoubleClickEvent(me, event):
        me.label.setText('mouseDoubleClickEvent')
    def contextMenuEvent(me, event):
        context = QMenu(me)
        context.addAction(QAction('Test 1', me))
        context.addAction(QAction('Test 2', me))
        context.addAction(QAction('Test 3', me))
        context.exec_(event.globalPos())
    
# Multithreading PyQt applications with QThreadPool
# https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
class WorkerThread(QRunnable):
    @QtCore.Slot() # not necessary?
    def run(me):
        print('Thread start')
        time.sleep(5)
        print('Thread complete')
class Worker(QRunnable):
    '''
    General worker class
    '''
    def __init__(me, fn, *args, **kwargs):
        super().__init__()
        me.fn = fn
        me.args = args
        me.kwargs = kwargs

    @QtCore.Slot()
    def run(me):
        me.fn(*me.args, **me.kwargs)

class MainWindowThread(QMainWindow):
    def __init__(me, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Thread pool
        me.threadpool = QThreadPool()
        print('Maximum {} threads'.format(me.threadpool.maxThreadCount()))

        me.counter = 0

        layout = QVBoxLayout()
        me.label = QLabel('Start')
        danger_button = QPushButton('DANGER!')
        danger_button.pressed.connect(me.oh_no)

        layout.addWidget(me.label)
        layout.addWidget(danger_button)

        w = QWidget()
        w.setLayout(layout)

        me.setCentralWidget(w)
        me.show()

        timer = me.timer = QTimer()
        timer.setInterval(1000)
        timer.timeout.connect(me.recurring_timer)
        timer.start()

    def oh_no(me):
        #time.sleep(5)
        def fn():
            print('Thread start')
            time.sleep(5)
            # sum = 0
            # for i in range(100000000):
            #     sum += i
            # print('Thread complete')
            
        worker = Worker(fn)
        me.threadpool.start(worker)
        
        # x = threading.Thread(target=fn)
        # x.start()

        # Cannot pickle error
        # x = Process(target=fn)
        # x.start()


    def recurring_timer(me):
        me.counter += 1
        me.label.setText('Counter: {}'.format(me.counter))

import sys
app = QApplication(sys.argv)
#window = MainWindow() #QWidget()
#window = MainWindow2()
#window = MainWindowThread()
#window = learnall.pyside2.MainWindow9()
window = learnall.pyside2.MainWindow36()
window.show()
app.exec_()
