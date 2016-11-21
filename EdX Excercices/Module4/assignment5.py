import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os

## add image plotting!


# Look pretty...
matplotlib.style.use('ggplot')

def Plot2D(T, title, x, y,colors, num_to_plot=40):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
#  for i in range(num_to_plot):
#    img_num = int(random.random() * num_images)
#    x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
#    x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
#    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
#    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7,c=colors)
  plt.show()
 
  
def Plot3D(T, title, x, y,z,colors, num_to_plot=40,):

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.set_zlabel('Component: {0}'.format(z))


  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
  z_size = (max(T[:,z]) - min(T[:,z])) * 0.08

#  for i in range(num_to_plot):
#    img_num = int(random.random() * num_images)
#    x0, y0,z0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.,T[img_num,z]
#    x1, y1,z1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.,T[img_num,z]
#    
#    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
#    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))



  ax.scatter(T[:,x],T[:,y],T[:,z], c=colors, marker='.')

  plt.show()
  
  
  
  
  
#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples=[]
colors=[]
for filename in os.listdir('Datasets/ALOI/32'):
    image=misc.imread('Datasets/ALOI/32/'+filename)
    samples.append((image / 255.0).reshape(-1))
    colors.append('b')

for filename in os.listdir('Datasets/ALOI/32i'):
    image=misc.imread('Datasets/ALOI/32i/'+filename)
    samples.append((image / 255.0).reshape(-1))
    colors.append('r')


#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 


df=pd.DataFrame(samples)

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 

from sklearn import manifold
iso=manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)

T=iso.transform(df)

Plot2D(T, "ISPMap plot of images reduced to 3 dimensions (plotting first 2)", 0, 1,colors, num_to_plot=100)
#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 




Plot3D(T,"3d Plot of Isomapped data",0,1,2,colors,num_to_plot=100)
#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

