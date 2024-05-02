# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:27:44 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt

num_steps = 1000;
rng = np.random.default_rng()

def createrandompath():
    x_step = rng.random(num_steps); #Creates a set of 500 random numbers from 0 to 1 for each array
    y_step = rng.random(num_steps);
    
    x_step = x_step > 0.5; #Converts these arrays to a series of 0s and 1s
    y_step = y_step > 0.5;
    
    x_step = 2*(((2*x_step + 1)/2) - 1) #Converts the 0s and 1s to -1s and 1s
    y_step = 2*(((2*y_step + 1)/2) - 1)
    
    x_dist = np.cumsum(x_step) #Takes the cumulative sum of each array
    y_dist = np.cumsum(y_step)
    return x_dist, y_dist
coordinates1_1A = createrandompath()

plt.plot(coordinates1_1A[0], coordinates1_1A[1]) #Creates plots
plt.plot(coordinates1_1A[0][0], coordinates1_1A[1][0], 'r+')
plt.plot(coordinates1_1A[0][-1], coordinates1_1A[1][-1], 'b+')
plt.grid()
plt.axis('equal')
plt.legend(['Position of Walker', 'Starting Point', 'Ending Point']);
plt.xlabel('Position in x Direction')
plt.ylabel('Postition in y Direction')
plt.title('Randomly Generated 2D Movement of a Walking Person')

#For the subplots, we want to use a consistent x and y scale, so this block of code finds the maximum x and y values to use.
coordinates1_1B1 = createrandompath()
coordinates1_1B2 = createrandompath()
coordinates1_1B3 = createrandompath()
coordinates1_1B4 = createrandompath()
allpositionvalues = np.concatenate((coordinates1_1B1[0], coordinates1_1B2[0], coordinates1_1B3[0], coordinates1_1B4[0], coordinates1_1B1[1], coordinates1_1B2[1], coordinates1_1B3[1], coordinates1_1B4[1]))
minvalue, maxvalue = min(allpositionvalues)-10, max(allpositionvalues)+10

#Subplots
fig2 = plt.figure()
plt.subplot(2,2,1)
plt.plot(coordinates1_1B1[0], coordinates1_1B1[1], 'r')
plt.plot(coordinates1_1B1[0][0], coordinates1_1B1[1][0], 'g+')
plt.plot(coordinates1_1B1[0][-1], coordinates1_1B1[1][-1], 'b+')
plt.grid()
plt.axis('square')
plt.xlim(minvalue, maxvalue)
plt.ylim(minvalue, maxvalue)
plt.legend(['Position of Walker', 'Starting Point', 'Ending Point']);
plt.xlabel('Position in x Direction')
plt.ylabel('Postition in y Direction')
plt.title('Randomly Generated 2D Movement of a Walking Person')

plt.subplot(2,2,2)
plt.plot(coordinates1_1B2[0], coordinates1_1B2[1], 'b')
plt.plot(coordinates1_1B2[0][0], coordinates1_1B2[1][0], 'r+')
plt.plot(coordinates1_1B2[0][-1], coordinates1_1B2[1][-1], 'g+')
plt.grid()
plt.axis('square')
plt.xlim(minvalue, maxvalue)
plt.ylim(minvalue, maxvalue)
plt.legend(['Position of Walker', 'Starting Point', 'Ending Point']);
plt.xlabel('Position in x Direction')
plt.ylabel('Postition in y Direction')
plt.title('Randomly Generated 2D Movement of a Walking Person')

plt.subplot(2,2,3)
plt.plot(coordinates1_1B3[0], coordinates1_1B3[1], 'm')
plt.plot(coordinates1_1B3[0][0], coordinates1_1B3[1][0], 'g+')
plt.plot(coordinates1_1B3[0][-1], coordinates1_1B3[1][-1], 'b+')
plt.grid()
plt.axis('square')
plt.xlim(minvalue, maxvalue)
plt.ylim(minvalue, maxvalue)
plt.legend(['Position of Walker', 'Starting Point', 'Ending Point']);
plt.xlabel('Position in x Direction')
plt.ylabel('Postition in y Direction')
plt.title('Randomly Generated 2D Movement of a Walking Person')

plt.subplot(2,2,4)
plt.plot(coordinates1_1B4[0], coordinates1_1B4[1], 'g')
plt.plot(coordinates1_1B4[0][0], coordinates1_1B4[1][0], 'r+')
plt.plot(coordinates1_1B4[0][-1], coordinates1_1B4[1][-1], 'b+')
plt.grid()
plt.axis('square')
plt.xlim(minvalue, maxvalue)
plt.ylim(minvalue, maxvalue)
plt.legend(['Position of Walker', 'Starting Point', 'Ending Point']);
plt.xlabel('Position in x Direction')
plt.ylabel('Postition in y Direction')
plt.title('Randomly Generated 2D Movement of a Walking Person')
plt.show()
