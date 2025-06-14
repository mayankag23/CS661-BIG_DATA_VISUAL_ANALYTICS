import vtk
from vtk import *

isovalue = float(input("give the isovalue"))

# Read the input VTI file
reader = vtkXMLImageDataReader()
reader.SetFileName("Isabel_2D.vti")
reader.Update()

data = reader.GetOutput()

dims = data.GetDimensions()
point_data = data.GetPointData().GetScalars()


contour_points = vtkPoints()
lines = vtkCellArray() #global

#Helper function to get id of point by coordinates
def idxy(i,j):
    return j*dims[0]+i

# Helper to get scalar value at a point by its coordinates
def get_value(i, j):
    return point_data.GetTuple1(idxy(i,j))

# Linear interpolation helper helper function
def lerp(p1, p2, v1, v2, iso):
    t = (iso - v1) / (v2 - v1)
    return [p1[i] + t * (p2[i] - p1[i]) for i in range(3)]

# Loop through each cell 
for j in range(dims[1] - 1):
    for i in range(dims[0] - 1):
        pt_ids = [
            idxy(i,j),           # bottom-left
            idxy(i+1,j),       # bottom-right
            idxy(i+1,j+1),   # top-right
            idxy(i,j+1)        # top-left
        ]
        pts = [data.GetPoint(pid) for pid in pt_ids]
        vals = [point_data.GetTuple1(pid) for pid in pt_ids]

        # Traverse edges counter clockwise
        ptcount = [] 
        for k in range(4):
            v1, v2 = vals[k], vals[(k + 1) % 4]
            if (v1 - isovalue) * (v2 - isovalue) < 0:  # Edge crosses isovalue
                p1, p2 = pts[k], pts[(k + 1) % 4]
                p_interp = lerp(p1, p2, v1, v2, isovalue)
                ptcount.append(contour_points.InsertNextPoint(p_interp))

        # Only draw a segment if 2 points are found
        if len(ptcount) == 2:
            line = vtkLine()
            line.GetPointIds().SetId(0, ptcount[0])
            line.GetPointIds().SetId(1, ptcount[1])
            lines.InsertNextCell(line)

# Create output polyData
polydata = vtkPolyData()
polydata.SetPoints(contour_points)
polydata.SetLines(lines)

# Write to .vtp file
writer = vtkXMLPolyDataWriter()
writer.SetFileName("isocontour2D.vtp")
writer.SetInputData(polydata)
writer.Write()


