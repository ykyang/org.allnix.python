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

# https://en.wikipedia.org/wiki/Web_colors
@fak.route('/vtk/v0/background/<string:color>', methods=['PUT'])
def background(color):
    vtkwin = config.vtkwindow
    renderer = vtkwin.renderer
    colors = vtk.vtkNamedColors()

    vtkwin.put_job(lambda : renderer.SetBackground(colors.GetColor3d(color)))
    vtkwin.put_job(lambda : vtkwin.render())

    response = fak.make_response(color)
    response.mimetype = "text/plain"
    
    return response

@fak.route('/red')
def red():
    vtkwin = config.vtkwindow
    renderer = vtkwin.renderer
    colors = vtk.vtkNamedColors()

    vtkwin.put_job(lambda : renderer.SetBackground(colors.GetColor3d('Red')))
    vtkwin.put_job(lambda : vtkwin.render())

    response = fak.make_response('red')
    response.mimetype = "text/plain"
    
    return response

@fak.route('/black')
def black():
    vtkwin = config.vtkwindow
    renderer = vtkwin.renderer
    colors = vtk.vtkNamedColors()

    vtkwin.put_job(lambda : renderer.SetBackground(colors.GetColor3d('Black')))
    vtkwin.put_job(lambda : vtkwin.render())
    
    
    response = fak.make_response('black')
    response.mimetype = "text/plain"
    
    return response