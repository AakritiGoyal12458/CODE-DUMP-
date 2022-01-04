"""The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (0,0) to (6,250), we have to pass two arrays [0, 6] and [0,250] to the plot function.
"""

import matplotlib.pyplot as plt
import numpy as np

#draw a line in a diagram from position (0,0) to position (6,250):

#(1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
"""xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])"""

"""(0,0) to (6,250)
xpoints=np.array([0,6])
ypoints=np.array([0,250])"""

#default x pointert66rrrrts
ypoints=np.array([3,8,1,10])
y1points=np.array([6,2,7,11])

##plt.plot(xpoints,ypoints,"o")
#plt.plot(ypoints,marker="o",ms=20)

##'o:r'
#format string marker|line(-,:,--,-.)|colour(r,g,b,c,m,y,k,w)
plt.plot(ypoints,marker="o",ms=20,mec='k',mfc='red',ls = ":",linewidth='20')
plt.plot(y1points)
plt.show()
