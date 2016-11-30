#
# TOOD: Import whatever needs to be imported to make this work
#
# .. your code here ..

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import date,time

matplotlib.style.use('ggplot') # Look Pretty


#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'



def doKMeans(df):
  #
  # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure(dpi=200)
  ax = fig.add_subplot(111)
  ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

  #
  # TODO: Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  # .. your code here ..
  newdf=df[['Longitude','Latitude']]
  print(newdf)
  #
  # TODO: Use K-Means to try and find seven cluster centers in this df.
  #
  # .. your code here ..
  kmeans_model=KMeans(n_clusters=7)
  kmeans_model.fit(newdf)
  #
  # INFO: Print and plot the centroids...
  centroids = kmeans_model.cluster_centers_
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  print centroids

  import gmplot

#  gmap = gmplot.GoogleMapPlotter(df.Latitude.mean(), df.Longitude.mean(), 10)
  gmap = gmplot.GoogleMapPlotter(df.Latitude.mean(), df.Longitude.mean(), 10)

  
  gmap.scatter(df.Latitude.tolist(), df.Longitude.tolist(), 'r', marker=False,size=100)
  gmap.scatter(centroids[:,1],centroids[:,0], c='k', marker=False,size=400)
  gmap.draw("chicago.html")


#
# TODO: Load your dataset after importing Pandas
#
# .. your code here ..

import pandas as pd

df=pd.read_csv('Datasets/Crimes_-_2001_to_present.csv')


#
# TODO: Drop any ROWs with nans in them
#
# .. your code here ..
df=df.dropna(axis=0)
df=df.reset_index()
#
# TODO: Print out the dtypes of your dset
#
# .. your code here ..
print (df.dtypes)

#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
# .. your code here ..
df.loc[:,'Date']=pd.to_datetime(df.loc[:,'Date'],errors='coerce')
print (df.dtypes)
# INFO: Print & Plot your data
doKMeans(df)


#
# TODO: Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
# .. your code here ..


df=df[df.Date>date(2011,1,1)]

# INFO: Print & Plot your data
doKMeans(df)
plt.show()

