Assignment 1 (Group Number - 9)

Group Member 1
Name - Mayank Agrawal
Roll No - 230639

Group Member 2
Name - Aryan Deo
Roll No - 230213

Group Member 3
Name - Ashutosh Anand
Roll No - 220239

Libraries Used:
VTK
(If not installed then install by opening the command prompt and type pip install vtk and hit enter)



1. Extract the "Assignment1.zip" in your local system.

2. The file contains the Data folder which we have the files Isabel_2D.vti and Isabel_3D.vti, pdf file Assignment_1, python source files Q1 and Q2 for respective first and second question, this README.md file, the output of first question vtkpolydata1.vtp file

3. For Question 1, 
How to run the isocontour script:
In the command prompt 
-Use python q1.py --input Isabel_2D.vti --output isocontour2D.vtp.
-Isabel_2D.vti is the input 2D VTK image file.
-isocontour2D.vtp is the output file containing extracted isocontours as vtkPolyData.
-The output can be opened directly in ParaView for visualization.
-Choose an isovalue between -1438 and 630 inside the script.
-Keep the input file in the same folder as the script, or update the path manually.
-Change the background color or overlay the input image when viewing the isocontour for better visibility.


4. For Question 2,
In VS Code
- Open the folder in VS Code containing Ques2.py and Isabel_3D.vti
- Open Ques2.py and click Run at the top right, or open a new terminal and run:
- This will execute the Python script. Input yes for Phong shading, else input no and press enter.


5. For Both question if you want to run on a different file then you need to give the path at specified location in the code.
