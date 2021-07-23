import sys
from threading import Thread
import queue

import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from PySide2 import QtCore
from PySide2.QtCore import QSize, QTimer, QRunnable, QThreadPool
from PySide2.QtWidgets import QApplication, QMainWindow

from learnall import vtkwindow
from learnall import fak
from learnall import config

# https://www.codegrepper.com/code-examples/python/run+flask+with+pyqt5
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()

    colors = vtk.vtkNamedColors()
    
    vtkwin = config.vtkwindow = vtkwindow.VtkWindow(window)
    window.setCentralWidget(vtkwin.interactor)

    cone = vtk.vtkConeSource()
    cone.SetResolution(8)

    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)

    vtkwin.renderer.AddActor(coneActor)

    window.show()

    colors = vtk.vtkNamedColors()
    vtkwin.interactor.Initialize()
    vtkwin.interactor.Start()
    def processvtk():
        try:
            fn = vtkwin.get_job()
            fn()
            #QTimer.singleShot(1, fn())
        except:
            pass # ignore Empty exception


    timer = QTimer()
    timer.setInterval(10)
    timer.timeout.connect(processvtk)
    timer.start()

    # https://www.codegrepper.com/code-examples/python/run+flask+with+pyqt5
    kwargs = {'host': '127.0.0.1', 'port': 5000, 'threaded': True, 'use_reloader': False, 'debug': True}
    fakThread = Thread(target=fak.run, daemon=True, kwargs=kwargs).start()


    app.exec_()

