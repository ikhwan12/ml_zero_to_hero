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

#Handle Missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean',axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#Deal with Categorical Data
