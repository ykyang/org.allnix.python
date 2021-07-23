from learnall import fak
#from flask import make_response

import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide2.QtCore import QTimer

from learnall import config

@fak.route('/hellovtk')
def hellovtk():
    response = fak.make_response('Hello VTK!')
    response.mimetype = "text/plain"
    return response

@fak.route('/red')
def red():
    vtkwin = config.vtkwindow
    renderer = vtkwin.renderer
    colors = vtk.vtkNamedColors()
    config.vtkque.put(lambda : renderer.SetBackground(colors.GetColor3d('Red')), block=False)
    config.vtkque.put(lambda : vtkwin.render())
    #QTimer.singleShot(1000, lambda : renderer.SetBackground(colors.GetColor3d('Red')))
    #QTimer.singleShot(2000, lambda : vtkwin.window.Render())
    # renderer.SetBackground(colors.GetColor3d('Red'))
    # vtkwin.window.Render()

    response = fak.make_response('red')
    response.mimetype = "text/plain"
    
    return response

@fak.route('/black')
def black():
    vtkwin = config.vtkwindow
    renderer = vtkwin.renderer
    colors = vtk.vtkNamedColors()

    config.vtkque.put(lambda : renderer.SetBackground(colors.GetColor3d('Black')), block=False)
    config.vtkque.put(lambda : vtkwin.render())
    
    
    response = fak.make_response('black')
    response.mimetype = "text/plain"
    
    return response