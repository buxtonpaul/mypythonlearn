# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 13:01:08 2016

@author: paul.buxton
"""

import matplotlib.pyplot as plt
import numpy as np

# create a data frame with random data

df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
# display as a correleation matrix comparing each field with all other fields
df.corr() 

# plot the correlation matrix using IMShow
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()