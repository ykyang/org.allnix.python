import vtk
# from paraview import *
from paraview.simple import *
from paraview.vtk.numpy_interface import dataset_adapter as dsa

# vtkPoints()
# poly = vtkPolyData()
# print(poly)
# Show(poly)


# cone = Cone()
# Show(cone)
# Render()
# Interact() # https://blog.kitware.com/interacting-with-views-in-paraview-python-pvpython/

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

c = dsa.PolyData(cylinderMapper)
#CreateView(cylinderActor)
Show(c)
Render()
Interact()
