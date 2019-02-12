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


def draw_first_lines(ax, p, length):
    #radius
    rad = length / 2
    
    #connects top point to bottom two points
    length = np.array([[p[0] - rad, p[1] - (2 * rad)], [p[0], p[1]], [p[0] + rad, p[1] - (2 * rad)]])
    
    #this creates plot big enough for the length
    ax.plot(length[:, 0], length[:, 1], color = 'k')

def draw_lines(ax, p, numPeaks, length):
    rad = length / 2 
    if numPeaks >= 2:
        
        #draws biggest peak(top peak)
        draw_first_lines(ax, p, length)
        
        #makes bottom points the new origins
        leftPoint = [p[0] - rad, p[1] - (rad * 2)]
        rightPoint = [p[0] + rad, p[1] - (rad * 2)]
        
        
        #Recursive calls
        draw_lines(ax, leftPoint, numPeaks - 1, length * .4)
        draw_lines(ax, rightPoint, numPeaks - 1, length * .4)
    
plt.close("all")
fig, ax = plt.subplots()

#Recursive call
draw_lines(ax, [0,0], 15, 2)

plt.show()
ax.set_aspect(3)
ax.axis('off')
fig.savefig('lines.png')