# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 13:26:12 2016

@author: paul.buxton
"""

import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')
student_dataset=pd.read_csv('Datasets/students.data',index_col=0)
student_dataset.head()
my_series=student_dataset.G3
my_dataframe=student_dataset[['G3','G2','G1']]
my_series
my_dataframe
my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)

# Normalise data to produce probabilites
my_dataframe.plot.hist(alpha=0.5,normed=True)
