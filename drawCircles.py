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


def draw_circles(ax, n, center, radius, w):
    if n > 0:
        x, y = circle(center, radius)
        
        #Creates plot to draw in
        ax.plot(x, y, color = 'k')
        
        #Decreases the center
        center[0] = center[0] - (radius * (1 - w))
        
        #Recursive call
        draw_circles(ax, n-1, center, radius * w, w)
        
        
plt.close("all") 
fig, ax = plt.subplots() 

#Recursive call
draw_circles(ax, 80, [50,0], 50,.94)

plt.show()
ax.set_aspect(1.0)
ax.axis('off')
fig.savefig('circles.png')