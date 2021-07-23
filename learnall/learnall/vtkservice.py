from learnall import fak
#from flask import make_response

import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

@fak.route('/hellovtk')
def hellovtk():
    response = fak.make_response('Hello VTK!')
    response.mimetype = "text/plain"
    return response

class VtkWindow():
    def __init__(me, parent):
        me.interactor = QVTKRenderWindowInteractor(parent)
        me.renderer = vtk.vtkRenderer()
        me.window = me.interactor.GetRenderWindow()
        me.window.AddRenderer(me.renderer)

if __name__ == '__main__':
    print('Hello VTK')