import vtk
#import tkinter
import time
import threading

# https://kitware.github.io/vtk-examples/site/
# See vtkInteractorStyle for key binding

def cylinder():
    colors = vtk.vtkNamedColors()
    # Set the background color.
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)
    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)
    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)
    # Create the graphics structure. The renderer renders into the render
    # window. The render window interactor captures mouse events and will
    # perform appropriate camera or actor manipulation depending on the
    # nature of the events.
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    ren.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(300, 300)
    
    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()
    # We'll zoom in a little by accessing the camera and invoking a "Zoom"
    # method on it.
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.SetWindowName('CylinderExample')
    renWin.Render()
    iren.Start()

def cone():
    colors = vtk.vtkNamedColors()

    cone = vtk.vtkConeSource()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cone.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d("bisque"))

    renderer = vtk.vtkRenderer()

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(renderer)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("Salmon"))

    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    iren.Initialize()
    # We'll zoom in a little by accessing the camera and invoking a "Zoom"
    # method on it.
    #ren.ResetCamera()
    #ren.GetActiveCamera().Zoom(1.5)
    renWin.SetSize(300, 300)
    renWin.SetWindowName("Cone")
    renWin.Render()
    iren.Start()


# https://kitware.github.io/vtk-examples/site/Python/Utilities/Animation/
# https://medium.com/@daniel.stjnv/animation-and-callbacks-with-vtk-dd4bd5e55c13
class vtkTimerCallback():
    def __init__(self, steps, actor, iren):
        self.timer_count = 0
        self.steps = steps
        self.actor = actor
        self.iren = iren
        self.timerId = None

    def execute(self, obj, event):
        step = 0
        while step < self.steps:
            print(self.timer_count)
            self.actor.SetPosition(self.timer_count / 100.0, self.timer_count / 100.0, 0)
            iren = obj
            iren.GetRenderWindow().Render()
            self.timer_count += 1
            step += 1
        if self.timerId:
            iren.DestroyTimer(self.timerId)
def animation():
    colors = vtk.vtkNamedColors()

    # Create a sphere
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(2)
    sphereSource.SetPhiResolution(30)
    sphereSource.SetThetaResolution(30)

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d("Peacock"))
    actor.GetProperty().SetSpecular(0.6)
    actor.GetProperty().SetSpecularPower(30)
    actor.SetMapper(mapper)
    # actor.SetPosition(-5, -5, 0)

    # Setup a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(colors.GetColor3d("MistyRose"))
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Animation")
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)

    # Render and interact
    renderWindow.Render()
    renderer.GetActiveCamera().Zoom(0.8)
    renderWindow.Render()

    # Initialize must be called prior to creating timer events.
    renderWindowInteractor.Initialize()

    # Sign up to receive TimerEvent
    cb = vtkTimerCallback(200, actor, renderWindowInteractor)
    renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
    cb.timerId = renderWindowInteractor.CreateRepeatingTimer(500)

    # start the interaction and timer
    renderWindow.Render()
    renderWindowInteractor.Start()


# https://kitware.github.io/vtk-examples/site/Python/Widgets/BoxWidget/
def boxCallback(obj, event):
    t = vtk.vtkTransform()
    obj.GetTransform(t)
    obj.GetProp3D().SetUserTransform(t)
    # type(event): str
    # event:InteractionEvent
def box():
    colors = vtk.vtkNamedColors()

    # Create a Cone
    cone = vtk.vtkConeSource()
    cone.SetResolution(20)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('BurlyWood'))

    # A renderer and render window
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('Blue'))
    renderer.AddActor(coneActor)

    renwin = vtk.vtkRenderWindow()
    renwin.AddRenderer(renderer)
    

    # An interactor
    interactor = vtk.vtkRenderWindowInteractor()
    #interactor = vtk.vtkGenericRenderWindowInteractor()
    interactor.SetRenderWindow(renwin)

    # A Box widget
    boxWidget = vtk.vtkBoxWidget()
    boxWidget.SetInteractor(interactor)
    boxWidget.SetProp3D(coneActor)
    boxWidget.SetPlaceFactor(1.25)  # Make the box 1.25x larger than the actor
    boxWidget.PlaceWidget()
    boxWidget.On()

    # Connect the event to a function
    # This call makes cone move and stretch with the box.
    # See complete list of event at 
    # https://vtk.org/doc/nightly/html/vtkCommand_8h_source.html
    boxWidget.AddObserver('InteractionEvent', boxCallback)

    # Start
    interactor.Initialize()
    renwin.SetWindowName('BoxWidget')
    renwin.Render()
    interactor.Start()
    #time.sleep(10)
    
def box_thread(renwin):
    colors = vtk.vtkNamedColors()

    # Create a Cone
    cone = vtk.vtkConeSource()
    cone.SetResolution(20)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('BurlyWood'))

    # A renderer and render window
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('Blue'))
    renderer.AddActor(coneActor)

    #renwin = vtk.vtkRenderWindow()
    renwin.AddRenderer(renderer)
    

    # An interactor
    interactor = vtk.vtkRenderWindowInteractor()
    #interactor = vtk.vtkGenericRenderWindowInteractor()
    interactor.SetRenderWindow(renwin)

    # A Box widget
    boxWidget = vtk.vtkBoxWidget()
    boxWidget.SetInteractor(interactor)
    boxWidget.SetProp3D(coneActor)
    boxWidget.SetPlaceFactor(1.25)  # Make the box 1.25x larger than the actor
    boxWidget.PlaceWidget()
    boxWidget.On()

    # Connect the event to a function
    # This call makes cone move and stretch with the box.
    # See complete list of event at 
    # https://vtk.org/doc/nightly/html/vtkCommand_8h_source.html
    boxWidget.AddObserver('InteractionEvent', boxCallback)
    
    # Start
    interactor.Initialize()
    renwin.SetWindowName('BoxWidget')
    renwin.Render()
    #time.sleep(2)
    interactor.Start()


## does not work, missing "vtkRenderingTk-8.90.dll"
def vtkRenderWindowInteractorConeExample():
    """Like it says, just a simple example
    https://gitlab.kitware.com/vtk/vtk/-/blob/master/Wrapping/Python/vtkmodules/tk/vtkTkRenderWindowInteractor.py
    """

    from vtkmodules.vtkFiltersSources import vtkConeSource
    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
    from vtkmodules.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor

    # create root window
    root = tkinter.Tk()

     # create vtkTkRenderWidget
    pane = vtkTkRenderWindowInteractor(root, width=300, height=300)
    pane.Initialize()

    def quit(obj=root):
        obj.quit()

    pane.AddObserver("ExitEvent", lambda o,e,q=quit: q())

    ren = vtkRenderer()
    pane.GetRenderWindow().AddRenderer(ren)

    cone = vtkConeSource()
    cone.SetResolution(8)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    # pack the pane into the tk root
    pane.pack(fill='both', expand=1)
    pane.Start()

    # start the tk mainloop
    root.mainloop()




def wxVTKRenderWindowInteractorConeExample(db):
    """Like it says, just a simple example
    https://discourse.vtk.org/t/interactor-start-blocking-execution/1095/2
    https://gitlab.kitware.com/vtk/vtk/-/blob/master/Wrapping/Python/vtkmodules/wx/wxVTKRenderWindowInteractor.py

    ipython --gui=wx
    #gui wx
    run learn_vtk.py
    
    Comment out 
    app.MainLoop()
    to run in ipython
    """

    from vtkmodules.vtkFiltersSources import vtkConeSource
    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
    from vtkmodules.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
    import wx

    colors = vtk.vtkNamedColors()

    # every wx app needs an app
    app = wx.App(False)

    # create the top-level frame, sizer and wxVTKRWI
    frame = wx.Frame(None, -1, "wxVTKRenderWindowInteractor", size=(400,400))
    widget = wxVTKRenderWindowInteractor(frame, -1)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(widget, 1, wx.EXPAND)
    frame.SetSizer(sizer)
    frame.Layout()
    db['interactor'] = widget

    # It would be more correct (API-wise) to call widget.Initialize() and
    # widget.Start() here, but Initialize() calls RenderWindow.Render().
    # That Render() call will get through before we can setup the
    # RenderWindow() to render via the wxWidgets-created context; this
    # causes flashing on some platforms and downright breaks things on
    # other platforms.  Instead, we call widget.Enable().  This means
    # that the RWI::Initialized ivar is not set, but in THIS SPECIFIC CASE,
    # that doesn't matter.
    widget.Enable(1)

    ren = vtkRenderer()
    renwin = widget.GetRenderWindow()
    widget.GetRenderWindow().AddRenderer(ren)
    db['renderer'] = ren
    db['render_window'] = renwin

    widget.AddObserver("ExitEvent", lambda o,e: renwin.Finalize())
    widget.AddObserver("ExitEvent", lambda o,e,f=frame: f.Close())

    cone = vtkConeSource()
    cone.SetResolution(8)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    # show the window
    frame.Show()
    # It works!
    # wx.CallLater(1000*5, lambda : ren.SetBackground(colors.GetColor3d('Blue')))
    # wx.CallLater(1000*8, lambda : renwin.Render())
    
    # colors = vtk.vtkNamedColors()
    # wx.CallAfter(lambda : ren.SetBackground(colors.GetColor3d('Blue')))
    # wx.CallAfter(lambda : renwin.Render())

    def fn():
       ren.SetBackground(colors.GetColor3d('Blue'))
       renwin.Render()
    wx.CallLater(1000*3, fn)
    

    app.MainLoop() # comment out to interact in ipython
    return wx, app, ren, renwin

# Not working, VTK still use gtk, too old?
def gtkVTKRenderWindowInteractorConeExample():
    from vtkmodules.vtkFiltersSources import vtkConeSource
    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
    from vtkmodules.gtk.GtkVTKRenderWindowInteractor import GtkVTKRenderWindowInteractor

    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk as gtk

    # The main window
    window = gtk.GtkWindow(gtk.WINDOW_TOPLEVEL)
    window.set_title("A GtkVTKRenderWindow Demo!")
    window.connect("destroy", gtk.mainquit)
    window.connect("delete_event", gtk.mainquit)
    window.set_border_width(10)

    # A VBox into which widgets are packed.
    vbox = gtk.GtkVBox(spacing=3)
    window.add(vbox)
    vbox.show()

    # The GtkVTKRenderWindow
    gvtk = GtkVTKRenderWindowInteractor()
    #gvtk.SetDesiredUpdateRate(1000)
    gvtk.set_usize(400, 400)
    vbox.pack_start(gvtk)
    gvtk.show()
    gvtk.Initialize()
    gvtk.Start()
    # prevents 'q' from exiting the app.
    gvtk.AddObserver("ExitEvent", lambda o,e,x=None: x)

    # The VTK stuff.
    cone = vtkConeSource()
    cone.SetResolution(80)
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    #coneActor = vtkLODActor()
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(0.5, 0.5, 1.0)
    ren = vtkRenderer()
    gvtk.GetRenderWindow().AddRenderer(ren)
    ren.AddActor(coneActor)

    # A simple quit button
    quit = gtk.GtkButton("Quit!")
    quit.connect("clicked", gtk.mainquit)
    vbox.pack_start(quit)
    quit.show()

    # show the main window and start event processing.
    window.show()
    gtk.mainloop()



def QVTKRenderWidgetConeExample():
    """A simple example that uses the QVTKRenderWindowInteractor class.
    https://gitlab.kitware.com/vtk/vtk/-/blob/master/Wrapping/Python/vtkmodules/qt/QVTKRenderWindowInteractor.py
    """

    from vtkmodules.vtkFiltersSources import vtkConeSource
    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
    # load implementations for rendering and interaction factory classes
    #import vtkmodules.vtkRenderingOpenGL2
    import vtkmodules.vtkInteractionStyle
    from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
    from PySide2 import QtCore, QtWidgets
    from PySide2.QtCore import QTimer

    # every QT app needs an app
    app = QtWidgets.QApplication(['QVTKRenderWindowInteractor'])

    window = QtWidgets.QMainWindow()

    colors = vtk.vtkNamedColors()

    # create the widget
    widget = QVTKRenderWindowInteractor(window)
    window.setCentralWidget(widget)
    # if you don't want the 'q' key to exit comment this.
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())

    renderer = vtkRenderer()
    widget.GetRenderWindow().AddRenderer(renderer)

    cone = vtkConeSource()
    cone.SetResolution(8)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    renderer.AddActor(coneActor)

    # show the widget
    window.show()

    widget.Initialize()
    
    # Use GUI thread to control VTK
    QTimer.singleShot(3000, lambda : renderer.SetBackground(colors.GetColor3d('Blue')))
    QTimer.singleShot(6000, lambda : renderer.SetBackground(colors.GetColor3d('Red')))
    
    widget.Start()

    # start event processing
    app.exec_()


print(vtk.vtkVersion.GetVTKVersion())
#cylinder()
#cone()
#animation()
#box()

db = {}
colors = vtk.vtkNamedColors()
#wx, app, ren, renwin = wxVTKRenderWindowInteractorConeExample(db)
#wx.CallAfter(lambda : ren.SetBackground(colors.GetColor3d('Red')))
#wx.CallAfter(lambda : renwin.Render())
#wx.CallAfter(lambda : ren.SetBackground(colors.GetColor3d('Blue')))

# renwin = vtk.vtkRenderWindow()
# x = threading.Thread(target=box_thread, args=(renwin,))
# x.start() # blocking, why?
# x.join()

QVTKRenderWidgetConeExample()