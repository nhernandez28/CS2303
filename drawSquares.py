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
from matplotlib.patches import Rectangle
#I got the above line of code, as well as line 18 and 21, from this link: 
#https://stackoverflow.com/questions/21445005/drawing-rectangle-with-border-only-in-matplotlib/21445448

def draw_squares(x, y, length, numTimes):
    #Creates plot to draw in
    ax.plot(100, 100, linewidth = 0.2, color = 'k')

    if numTimes == 1:
        #Draws the initial rectangle
        currAx.add_patch(Rectangle((x, y), length, length, alpha = 1, Fill = None))
        
    elif numTimes > 1:
        currAx.add_patch(Rectangle((x, y), length, length, alpha = 1, Fill = None))
        
        #top left
        draw_squares(x - length / 4, y + (length - length / 4), length * .5, numTimes - 1)
        #top right
        draw_squares(x + (length - length / 4), y + (length - length / 4), length * .5, numTimes - 1)
        #bottom right corner
        draw_squares(x + (length-length / 4), y - length / 4, length * .5, numTimes - 1) 
        #bottom left
        draw_squares(x - length / 4, y - length / 4, length * .5, numTimes - 1)
        
        
fig, ax = plt.subplots()
ax.axis('off')
currAx = plt.gca() 
plt.show()

#Recursive call 
draw_squares(50, 50, 50, 3)