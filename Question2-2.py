# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:02:49 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

#Preforms Simulation
def unfaircoinflip():
    samples = rng.random(100)
    flips = samples < 0.08;
    indices = np.nonzero(flips)
    timedifference = np.diff(indices)
    return timedifference

#Plots Data from Simulation
def timeintervals(numtrials):
    M = np.zeros(0)
    for i in range(numtrials):
        M = np.append(M, unfaircoinflip())
    plt.hist(M)
    plt.semilogy()
    plt.xlabel('Waiting Time between Heads')
    plt.ylabel('Log of Frequency')
    plt.title('A plot of waiting times between heads in an unfair coin flip')
    print(f'The average waiting time between heads is {np.average(M)}.')
    return

#Calls for data to be plotted for two different trial amounts
timeintervals(1000)
timeintervals(1000000)