"""
CS2302
Lab1
Purpose: learn how to use recursion to create figures, get familiar with python, learn how to use matplotlib
Created on Wed Jan 30, 2019
Last modified Mon Feb 11, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

#provided code
def circle(center, rad):
    n = int(4 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    
    return x, y


def draw_mult_circles(ax, numTimes, center, radius):
    if numTimes > 0:
       x, y = circle(center, radius)
       
       #Creates plot to draw in
       ax.plot(x, y, color = 'k')
       
       #Draws center circle
       draw_mult_circles(ax, numTimes - 1, center, radius * (1 / 3))
       
       #draws circle on left side of center
       radLeft = [center[0] - (radius * (2 / 3)), center[1]]
       
       #draws circle Above center
       radUp = [center[0], (radius * (2 / 3)) + center[1]]
       
       #draws circle on Right side of center
       radRight = [(radius * (2 / 3)) + center[0], center[1]]
       
       #draws circle Below center
       radDown = [center[0], center[1] - (radius * (2 / 3))]
        
       
       #Recursive calls that create figure
       draw_mult_circles(ax, numTimes - 1, radLeft, (1 / 3) * radius)
       
       draw_mult_circles(ax, numTimes - 1, radUp, (1 / 3) * radius)
       
       draw_mult_circles(ax, numTimes - 1, radRight, (1 / 3) * radius)
       
       draw_mult_circles(ax, numTimes - 1, radDown, (1 / 3) * radius)
       
        
plt.close("all") 
fig, ax = plt.subplots() 

#Recursive call
draw_mult_circles(ax, 5, [0,0], 100)

plt.show()
ax.set_aspect(1.0)
ax.axis('off')
fig.savefig('circles.png')