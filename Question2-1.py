# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:18:00 2024

@author: mdubo
"""

import math
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

#Math for Poisson Distribution
def poissondist(heads, prob):
    return ((np.exp(-prob)*prob**heads)/math.factorial(heads))

poissonlist = np.zeros(50)
for l in range(50):
    poissonlist[l] = float(poissondist(l, 8))

#Plots Poisson Distribution
plt.plot(poissonlist)
plt.xlabel('Amount of Times the Coin is Flipped on Heads')
plt.ylabel('Probability of This Occurance')
plt.title('Probability of a Coin Being Flipped and landing on Heads')

#Preforms Simulation
def unfaircoinflip():
    samples = rng.random(100)
    flips = samples < 0.08;
    heads = np.sum(flips)
    tails = 100 - heads
    return heads, tails

#Plots data from simulation
def experimentaldata(N):
    M = np.zeros(N)
    for i in range(N):
        M[i] = unfaircoinflip()[0]
    fig2 = plt.figure()
    plt.hist(M, 100, [0, 100])
    plt.xlabel('Number of Heads In Each Trial')
    plt.ylabel('Frequency of this Result')
    plt.title(f'Number of Heads after 100 flips of an Unfair Coin Performed {N} Times.')
    plt.plot(poissonlist*N)
    plt.legend(['Poisson Distribution', 'Simulation'])
    return

#Calls for data to be plotted for two different trial amounts
experimentaldata(1000)
experimentaldata(1000000)


    
    
    