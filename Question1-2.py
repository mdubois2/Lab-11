# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:35:16 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt

num_steps1 = 1000;
num_steps2 = 4000;
num_walks = 1000;
rng = np.random.default_rng()

def createrandompath(stepsize):
    x_step = rng.random(stepsize); #Creates a set of 500 random numbers from 0 to 1 for each array
    y_step = rng.random(stepsize);
    
    x_step = x_step > 0.5; #Converts these arrays to a series of 0s and 1s
    y_step = y_step > 0.5;
    
    x_step = 2*(((2*x_step + 1)/2) - 1) #Converts the 0s and 1s to -1s and 1s
    y_step = 2*(((2*y_step + 1)/2) - 1)
    
    x_dist = np.cumsum(x_step) #Takes the cumulative sum of each array
    y_dist = np.cumsum(y_step)
    return x_dist, y_dist

#Declares arrays to be used later
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)

#Solves for displacements of different trials
for i in range(num_walks):
    walki = createrandompath(num_steps1)
    x_final[i] = walki[0][-1]
    y_final[i] = walki[1][-1]
    displacement[i] = np.sqrt((walki[0][-1])**2 + ((walki[1][-1])**2))

#Plots
plt.scatter(x_final, y_final)
plt.grid()
plt.axis('equal')
plt.xlabel('Final x Position of Walkers')
plt.ylabel('Final y Position of Walkers')
plt.title('Final Position of 1,000 Different Walkers')

fig2 = plt.figure()
plt.hist(displacement)
plt.xlabel('Displacement of Walker')
plt.ylabel('Frequency')
plt.title('Displacements of 1000 Different Walkers')

fig3 = plt.figure()
plt.hist(displacement**2)
plt.xlabel('Displacement of Walker Squared')
plt.ylabel('Frequency')
plt.title('The Displacement Squared of 1000 Different Walkers')

fig4 = plt.figure()
plt.hist(displacement**2)
plt.xlabel('Displacement of Walker Squared')
plt.ylabel('log(Frequency)')
plt.title('The Displacement Squared of 1000 Different Walkers')
plt.semilogy()

print(f"The mean displacement^2 value is {np.mean(displacement**2)} for a sample size of 1000 walkers.")

for i in range(num_walks):
    walki = createrandompath(num_steps2)
    x_final[i] = walki[0][-1]
    y_final[i] = walki[1][-1]
    displacement[i] = np.sqrt((walki[0][-1])**2 + ((walki[1][-1])**2))

print(f"The mean displacement^2 value is {np.mean(displacement**2)} for a sample size of 4000 walkers.")
''' The relationship between the number of walks and the displacement^2 value seems to be 1:2'''