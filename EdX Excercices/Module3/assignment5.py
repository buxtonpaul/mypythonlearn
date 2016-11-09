import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

# Look pretty...
matplotlib.style.use('ggplot')


seeds = pd.read_csv("Datasets/wheat.data", index_col=0)





#seeds=seeds.drop(labels=['area','perimeter'],axis=1)

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..

plt.figure(dpi=267)
andrews_curves(seeds, 'wheat_type',alpha=4)

plt.show()


