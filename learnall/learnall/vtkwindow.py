import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VtkWindow():
    def __init__(me, parent):
        me.interactor = QVTKRenderWindowInteractor(parent)
        me.renderer = vtk.vtkRenderer()
        me.window = me.interactor.GetRenderWindow()
        me.window.AddRenderer(me.renderer)

if __name__ == '__main__':
    print('Hello VTK')