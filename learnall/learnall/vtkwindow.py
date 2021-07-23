import queue

import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VtkWindow():
    def __init__(me, parent):
        me.interactor = QVTKRenderWindowInteractor(parent)
        me.renderer = vtk.vtkRenderer()
        me.window = me.interactor.GetRenderWindow()
        me.window.AddRenderer(me.renderer)
        me.job_queue = queue.Queue()

    def add_actor(me, actor):
        me.renderer.AddActor(actor)
    def render(me):
        me.window.Render()
    def put_job(me, job):
        me.job_queue.put(job, block=False)
    def get_job(me):
        try:
            job = me.job_queue.get(block=False)
        except:
            job = lambda : None
        
        return job
    
    
# python -m learnall.vtkwindow
if __name__ == '__main__':
    print('Hello VTK')