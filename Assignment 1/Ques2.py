
# Import VTK library
from vtk import *

# Load the .vti data file (Isabel hurricane dataset)
vti_reader = vtkXMLImageDataReader()
vti_reader.SetFileName("Isabel_3D.vti")    #this file should be in the same directory
vti_reader.Update()

# Volume mapper setup
volume_mapper = vtkSmartVolumeMapper()
volume_mapper.SetInputConnection(vti_reader.GetOutputPort())

# Design color and opacity map
vol_property = vtkVolumeProperty()
color_map = vtkColorTransferFunction()

# Assign scalar values to colors (based on domain knowledge or trial/error)
color_map.AddRGBPoint(-4931.5, 0.0, 1.0, 1.0)  #light blue
color_map.AddRGBPoint(-2508.9, 0.0, 0.0, 1.0)  #blue
color_map.AddRGBPoint(-1873.9, 0.0, 0.0, 0.5)  #dark blue
color_map.AddRGBPoint(-1027.1, 1.0, 0.0, 0.0)  #red
color_map.AddRGBPoint(-298.0,  1.0, 0.4, 0.0)  #orange
color_map.AddRGBPoint(2595.0,  1.0, 1.0, 0.0)  #yellow

opacity_map = vtkPiecewiseFunction()
opacity_map.AddPoint(-4931.5, 1.0)    #full visible
opacity_map.AddPoint(101.8,   0.002)  #some transparent
opacity_map.AddPoint(2595.0,  0.0)    #full transparent

# Applying color and opacity mapping to the volume property
vol_property.SetColor(color_map)
vol_property.SetScalarOpacity(opacity_map)

# User Input: enable Phong shading
enable_shading = input("Enable Phong shading? (yes/no): ").strip().lower()
if enable_shading == "yes":
    vol_property.ShadeOn()
    vol_property.SetAmbient(0.5)
    vol_property.SetDiffuse(0.5)
    vol_property.SetSpecular(0.5)
    vol_property.SetSpecularPower(10.0)
else:
    vol_property.ShadeOff()

#Volume actor Creating
volume_actor = vtkVolume()
volume_actor.SetMapper(volume_mapper)
volume_actor.SetProperty(vol_property)

# Outline around the volume for better spatial perception
outline = vtkOutlineFilter()
outline.SetInputConnection(vti_reader.GetOutputPort())

outline_mapper = vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline.GetOutputPort())

outline_actor = vtkActor()
outline_actor.SetMapper(outline_mapper)
outline_actor.GetProperty().SetColor(0, 0, 0)  # Black outline

# Rendering setup
scene_renderer = vtkRenderer()
scene_renderer.SetBackground(255, 237, 217) # For background

scene_renderer.AddVolume(volume_actor)
scene_renderer.AddActor(outline_actor)

# for render window setup
render_win = vtkRenderWindow()
render_win.AddRenderer(scene_renderer)
render_win.SetSize(1000, 1000)

# for interaction setup
viewer = vtkRenderWindowInteractor()
viewer.SetRenderWindow(render_win)

# Start interactive rendering
viewer.Initialize()
viewer.Start()
