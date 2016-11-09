import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

seeds = pd.read_csv("Datasets/wheat.data", index_col=0)


#
# TODO: Drop the 'id' feature
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..

plt.imshow(seeds.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(seeds.columns))]
plt.xticks(tick_marks, seeds.columns, rotation='vertical')
plt.yticks(tick_marks, seeds.columns)

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..


plt.show()


