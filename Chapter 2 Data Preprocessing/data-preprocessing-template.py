# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:05:55 2020

@author: ikhwa
"""

#Data Preprocessing
#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("data.csv")

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values