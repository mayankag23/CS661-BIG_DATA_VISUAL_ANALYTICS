# Import VTK library
import vtk

# Load the .vti data file (Isabel hurricane dataset)
vti_reader = vtk.vtkXMLImageDataReader()
vti_reader.SetFileName("Isabel_3D.vti")
vti_reader.Update()

# Volume mapper setup
volume_mapper = vtk.vtkSmartVolumeMapper()
volume_mapper.SetInputConnection(vti_reader.GetOutputPort())

# Design color and opacity map
vol_property = vtk.vtkVolumeProperty()
color_map = vtk.vtkColorTransferFunction()

# Assign scalar values to colors (based on domain knowledge or trial/error)
color_map.AddRGBPoint(-4931.5, 0.0, 1.0, 1.0) 
color_map.AddRGBPoint(-2508.9, 0.0, 0.0, 1.0) 
color_map.AddRGBPoint(-1873.9, 0.0, 0.0, 0.5) 
color_map.AddRGBPoint(-1027.1, 1.0, 0.0, 0.0)  
color_map.AddRGBPoint(-298.0,  1.0, 0.4, 0.0)  
color_map.AddRGBPoint(2595.0,  1.0, 1.0, 0.0)  

opacity_map = vtk.vtkPiecewiseFunction()
opacity_map.AddPoint(-4931.5, 1.0)
opacity_map.AddPoint(101.8,   0.002)
opacity_map.AddPoint(2595.0,  0.0)

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
volume_actor = vtk.vtkVolume()
volume_actor.SetMapper(volume_mapper)
volume_actor.SetProperty(vol_property)

# Outline around the volume for better spatial perception
outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(vti_reader.GetOutputPort())

outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline.GetOutputPort())

outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)
outline_actor.GetProperty().SetColor(0, 0, 0)  # Black outline

# Rendering setup
scene_renderer = vtk.vtkRenderer()
scene_renderer.SetBackground(255, 237, 217) # For background

scene_renderer.AddVolume(volume_actor)
scene_renderer.AddActor(outline_actor)

render_win = vtk.vtkRenderWindow()
render_win.AddRenderer(scene_renderer)
render_win.SetSize(1000, 1000)

# Interaction setup
viewer = vtk.vtkRenderWindowInteractor()
viewer.SetRenderWindow(render_win)

# Start interactive rendering
viewer.Initialize()
viewer.Start()