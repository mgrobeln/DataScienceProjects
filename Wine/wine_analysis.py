#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:44:54 2020

@author: Marlena
"""

import csv 
import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sb


dataset = []

with open('/Users/Marlena/Desktop/DataScienceProjects/Wine/winequality-red.csv') as file:
    csv_reader = csv.reader(file, delimiter=";")
    
    for d in csv_reader:
        
        dataset.append(d)
dataframe = pd.DataFrame(dataset[1:])

dataframe.columns = [dataset[0]]
dataframe = dataframe.astype(np.float)


#plot alcohol and quality
alc = dataframe['alcohol']
alc.plot()
plt.show()


average = dataframe.mean()

std = dataframe.std()

sb.distplot(alc)



#sb.pairplot(dataframe)

dataframe.boxplot()