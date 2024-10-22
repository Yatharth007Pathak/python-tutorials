# Indian flag using python

import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend

import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((0, 1), width = 9, height = 2, facecolor = '#138808', edgecolor = 'grey')
b = patch.Rectangle((0, 3), width = 9, height = 2, facecolor = '#ffffff', edgecolor = 'grey')
c = patch.Rectangle((0, 5), width = 9, height = 2, facecolor = '#FF6103', edgecolor = 'grey')
m, n = py.subplots()
n.add_patch(a) 
n.add_patch(b)
n.add_patch(c)

radius = 0.8
py.plot(4.5, 4, marker = 'o', markerfacecolor = '#000080', markersize = 9.5) 
chakra = py.Circle((4.5, 4), radius, color='#000080', fill = False, linewidth = 7)
n.add_artist(chakra)

for i in range(0, 24):
    p = 4.5 + radius/2 * np.cos(np.pi * i/9 + np.pi/48) 
    q = 4.5 + radius/2 * np.cos(np.pi * i/9 - np.pi/48)
    r = 4 + radius/2 * np.sin(np.pi * i/9 + np.pi/48)
    s = 4 + radius/2 * np.sin(np.pi * i/9 - np.pi/48)
    t = 4.5 + radius * np.cos(np.pi * i/9)
    u = 4 + radius * np.sin(np.pi * i/9)
    n.add_patch(patch.Polygon([[4.5, 4], [p, r], [t, u], [q, s]], fill = True, closed = True, color = '#000080'))

py.axis('equal')
py.show()

'''
Here's a line-by-line breakdown of the code:

import matplotlib 
matplotlib.use('TkAgg')  # Use the TkAgg backend
Importing Matplotlib: This imports the Matplotlib library.
Setting Backend: This specifies the backend to use for rendering the plot. 'TkAgg' is a common choice for interactive plots.

import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
Importing NumPy: This imports the NumPy library, which is useful for numerical operations, particularly with arrays.
Importing Matplotlib's Pyplot: This imports the pyplot module from Matplotlib, allowing for easy plotting.
Importing Patches: This imports the patches module from Matplotlib, which provides classes for creating shapes (like rectangles and circles).

a = patch.Rectangle((0, 1), width = 9, height = 2, facecolor = '#138808', edgecolor = 'grey')
Creating Rectangle a: This creates a rectangle (a) starting at the coordinate (0, 1) with a width of 9 and a height of 2. 
The rectangle is filled with a green color (#138808) and has a grey edge.

b = patch.Rectangle((0, 3), width = 9, height = 2, facecolor = '#ffffff', edgecolor = 'grey')
Creating Rectangle b: This creates another rectangle (b) starting at (0, 3) with the same width and height as a. 
This rectangle is filled with white (#ffffff) and also has a grey edge.

c = patch.Rectangle((0, 5), width = 9, height = 2, facecolor = '#FF6103', edgecolor = 'grey')
Creating Rectangle c: This creates a third rectangle (c) starting at (0, 5) with the same dimensions. 
It is filled with orange color (#FF6103) and has a grey edge.

m, n = py.subplots()
Creating Subplots: This creates a figure and a set of subplots. m is the figure object, and n is the axes object where the shapes will be drawn.

n.add_patch(a) 
n.add_patch(b)
n.add_patch(c)
Adding Rectangles to Axes: These lines add the previously created rectangles (a, b, and c) to the axes n.

radius = 0.8
Setting Radius: This defines a radius for circles or other shapes that will be drawn later.

py.plot(4.5, 4, marker = 'o', markerfacecolor = '#000080', markersize = 9.5) 
Plotting a Point: This plots a point at coordinates (4.5, 4) using a blue color (#000080) with a specified marker size.

chakra = py.Circle((4.5, 4), radius, color='#000080', fill = False, linewidth = 7)
Creating Circle (Chakra): This creates a circle (chakra) centered at (4.5, 4) with the specified radius. 
It is outlined with a blue color and has a line width of 7. The fill parameter is set to False, so the circle will not be filled.

n.add_artist(chakra)
Adding Circle to Axes: This adds the circle (chakra) to the axes n.

for i in range(0, 24):
Looping: This begins a loop that will iterate 24 times, which is likely to create multiple shapes or patterns around the circle.

p = 4.5 + radius/2 * np.cos(np.pi * i/9 + np.pi/48) 
q = 4.5 + radius/2 * np.cos(np.pi * i/9 - np.pi/48)
r = 4 + radius/2 * np.sin(np.pi * i/9 + np.pi/48)
s = 4 + radius/2 * np.sin(np.pi * i/9 - np.pi/48)
t = 4.5 + radius * np.cos(np.pi * i/9)
u = 4 + radius * np.sin(np.pi * i/9)
Calculating Coordinates: Within the loop, these lines calculate coordinates for points p, q, r, s, t, and u.
p and q are x-coordinates adjusted by cosine functions.
r and s are y-coordinates adjusted by sine functions.
t and u represent the coordinates for another point at a larger radius.

n.add_patch(patch.Polygon([[4.5, 4], [p, r], [t, u], [q, s]], fill = True, closed = True, color = '#000080'))
Adding Polygon: This line creates a polygon using the calculated coordinates and adds it to the axes n. 
The polygon is filled with blue color and is closed, meaning its last point connects back to the first.

py.axis('equal')
Setting Equal Aspect Ratio: This sets the aspect ratio of the plot to be equal, ensuring that circles look like circles rather than ellipses.

py.show()
Displaying the Plot: This line renders and displays the plot created with all the shapes and configurations.
'''