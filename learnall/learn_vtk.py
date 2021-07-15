import vtk

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


#cylinder()
#cone()
#animation()
box()


