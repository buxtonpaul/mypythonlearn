import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

seeds = pd.read_csv("Datasets/wheat.data", index_col=0)



#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
<<<<<<< HEAD
seeds=pd.read_csv('Datasets/wheat.data')
=======
fig = plt.figure(dpi=267)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
>>>>>>> da63770e040c916ab937e9d84982297a800db0c9

ax.scatter(seeds.area, seeds.perimeter, seeds.asymmetry, c='red', marker='.')

<<<<<<< HEAD
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Asymmetry')

ax.scatter(seeds.area, seeds.perimeter, seeds.asymmetry, c='red', marker='.')

fig = plt.figure()
=======
fig = plt.figure(dpi=267)
>>>>>>> da63770e040c916ab937e9d84982297a800db0c9
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')

ax.scatter(seeds.width, seeds.groove, seeds.length, c='green', marker='.')

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Width')
ax.set_ylabel('Groove')
ax.set_zlabel('Length')

ax.scatter(seeds.width, seeds.groove, seeds.length, c='green', marker='.')


plt.show()


