import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from datetime import date,time
import datetime
import gmplot


matplotlib.style.use('ggplot') # Look Pretty

def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
  exit()


  
def HandleUser(UserID, cdr_df):
    
    userdata=cdr_df[cdr_df.In==UserID]

    # INFO: Plot all the call locations
    plottitle='Call locations for user {0}'.format(UserID)
#    userdata.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title=plottitle)
    
    #toto use gmplot to sdee on map!

#    gmap = gmplot.GoogleMapPlotter(userdata.TowerLat.mean(), userdata.TowerLon.mean(), 10)

#    gmap.scatter(userdata.TowerLat.tolist(), userdata.TowerLon.tolist(), 'r', marker=False)
    userdata=userdata[(userdata.DOW=='Sat') | (userdata.DOW=='Sun')]
    userdata=userdata[(userdata.CallTime<datetime.timedelta(hours=6)) | (userdata.CallTime>=datetime.timedelta(hours=22))]
    
    userdata.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title='Call Locations')

                      
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(user1.TowerLon.tolist(),user1.TowerLat.tolist(), c='g', marker='o', alpha=0.2)
    #ax.set_title('Weekend Calls (<6am or >10p)')

#    gmap.scatter(userdata.TowerLat.tolist(), userdata.TowerLon.tolist(), 'k', marker=False,size=400)
    #gmap.draw("mymap.html")


    newdf=userdata[['TowerLat','TowerLon']]
    #print(newdf)
    kmeans_model=KMeans(n_clusters=1)
    kmeans_model.fit(newdf)
    
      # INFO: Print and plot the centroids...
    centroids = kmeans_model.cluster_centers_
  #  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)

    #  gmap = gmplot.GoogleMapPlotter(df.Latitude.mean(), df.Longitude.mean(), 10)
    gmap = gmplot.GoogleMapPlotter(newdf.TowerLat.mean(), newdf.TowerLon.mean(), 10)

  
    #gmap.scatter(newdf.TowerLat.tolist(), newdf.TowerLon.tolist(), 'r', marker=False,size=100)
    gmap.scatter(centroids[:,0],centroids[:,1], 'r', marker=False,size=400)
    htmltitle='user_{0}.html'.format(UserID)
    gmap.draw(htmltitle)


  


#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live and work at!
cdr_df=pd.read_csv("Datasets/CDR.csv")
cdr_df.head()
cdr_df.dtypes

#
# TODO: Load up the dataset and take a peek at its head
# Convert the date using pd.to_datetime, and the time using pd.to_timedelta
#
# .. your code here ..

cdr_df.CallDate=pd.to_datetime(cdr_df.CallDate)
cdr_df.CallTime=pd.to_timedelta(cdr_df.CallTime)
cdr_df.Duration=pd.to_timedelta(cdr_df.Duration)

#
# TODO: Get a distinct list of "In" phone numbers (users) and store the values in a
# regular python list.
# Hint: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
#
# .. your code here ..
list=cdr_df.In.unique().tolist()


# 
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above
#
# .. your code here ..




#gmap.heatmap(user1.TowerLat.tolist(), user1.TowerLon.tolist())


print list

#user1=user1[(user1.CallTime<datetime.timedelta(hours=6)) | (user1.CallTime>=datetime.timedelta(hours=22))]



#
# INFO: Visualize the dataframe with a scatter plot as a sanity check. Since you're familiar
# with maps, you know well that your X-Coordinate should be Longitude, and your Y coordinate
# should be the tower Latitude. Check the dataset headers for proper column feature names.
# https://en.wikipedia.org/wiki/Geographic_coordinate_system#Geographic_latitude_and_longitude
#
# At this point, you don't yet know exactly where the user is located just based off the cell
# phone tower position data; but considering the below are for Calls that arrived in the twilight
# hours of weekends, it's likely that wherever they are bunched up is probably near where the
# caller's residence:
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(user1.TowerLon.tolist(),user1.TowerLat.tolist(), c='g', marker='o', alpha=0.2)
#ax.set_title('Weekend Calls (<6am or >10p)')
#showandtell()  # TODO: Comment this line out when you're ready to proceed


for user in list:
    HandleUser(user,cdr_df)
