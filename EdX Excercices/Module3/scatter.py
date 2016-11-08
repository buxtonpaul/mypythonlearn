# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 07:44:29 2016

@author: paulb
"""

import pandas as pd
import matplotlib

matplotlib.style.use('ggplot')
student_dataset=pd.read_csv('Datasets/students.data',index_col=0)
student_dataset.head()
student_dataset.plot.scatter('G1','G2',figsize=(8,8))
