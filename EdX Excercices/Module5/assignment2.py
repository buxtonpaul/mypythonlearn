import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from datetime import date,time
import gmplot


matplotlib.style.use('ggplot') # Look Pretty

def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
  exit()




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




user1=cdr_df[cdr_df.In==list[0]]

# INFO: Plot all the call locations
user1.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title='Call Locations')

#toto use gmplot to sdee on map!

gmap = gmplot.GoogleMapPlotter(user1.TowerLat.mean(), user1.TowerLon.mean(), 10)

#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
gmap.scatter(user1.TowerLat.tolist(), user1.TowerLon.tolist(), 'r', marker=False)
#gmap.heatmap(user1.TowerLat.tolist(), user1.TowerLon.tolist())


print list

#showandtell()  # Comment this line out when you're ready to proceed


#
# INFO: The locations map above should be too "busy" to really wrap your head around. This
# is where domain expertise comes into play. Your intuition tells you that people are likely
# to behave differently on weekends:
#
# On Weekdays:
#   1. People probably don't go into work
#   2. They probably sleep in late on Saturday
#   3. They probably run a bunch of random errands, since they couldn't during the week
#   4. They should be home, at least during the very late hours, e.g. 1-4 AM
#
# On Weekdays:
#   1. People probably are at work during normal working hours
#   2. They probably are at home in the early morning and during the late night
#   3. They probably spend time commuting between work and home everyday

#
# TODO: Add more filters to the user1 slice you created. Add bitwise logic so that you're
# only examining records that came in on weekends (sat/sun).
#
# .. your code here ..
user1=user1[(user1.DOW=='Sat') | (user1.DOW=='Sun')]


#
# TODO: Further filter it down for calls that are came in either before 6AM OR after 10pm (22:00:00).
# You can use < and > to compare the string times, just make sure you code them as military time
# strings, eg: "06:00:00", "22:00:00": https://en.wikipedia.org/wiki/24-hour_clock
#
# You might also want to review the Data Manipulation section for this. Once you have your filtered
# slice, print out its length:
#
# .. your code here ..

user1=user1[(user1.CallTime<datetime.timedelta(hours=6)) | (user1.CallTime>=datetime.timedelta(hours=22))]



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
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(user1.TowerLon.tolist(),user1.TowerLat.tolist(), c='g', marker='o', alpha=0.2)
ax.set_title('Weekend Calls (<6am or >10p)')
#showandtell()  # TODO: Comment this line out when you're ready to proceed

# note that gmap uses lat followed by long
gmap.scatter(user1.TowerLat.tolist(), user1.TowerLon.tolist(), 'k', marker=False,size=400)

gmap.draw("mymap.html")


#
# TODO: Run K-Means with a K=1. There really should only be a single area of concentration. If you
# notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
# apart from one another), then increase K=2, with the goal being that one of the centroids will
# sweep up the annoying outliers; and the other will zero in on the user's approximate home location.
# Or rather the location of the cell tower closest to their home.....
#
# Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
# data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
# no feature scaling is required. Print out the centroid locations and add them onto your scatter
# plot. Use a distinguishable marker and color.
#
# Hint: Make sure you graph the CORRECT coordinates. This is part of your domain expertise.
#
# .. your code here ..


#showandtell()  # TODO: Comment this line out when you're ready to proceed
newdf=user1[['TowerLat','TowerLon']]
#print(newdf)
  #
  # TODO: Use K-Means to try and find seven cluster centers in this df.
  #
  # .. your code here ..
kmeans_model=KMeans(n_clusters=1)
kmeans_model.fit(newdf)
 #
  # INFO: Print and plot the centroids...
centroids = kmeans_model.cluster_centers_
ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
#print centroids

#  gmap = gmplot.GoogleMapPlotter(df.Latitude.mean(), df.Longitude.mean(), 10)
gmap = gmplot.GoogleMapPlotter(newdf.TowerLat.mean(), newdf.TowerLon.mean(), 10)

  
#gmap.scatter(newdf.TowerLat.tolist(), newdf.TowerLon.tolist(), 'r', marker=False,size=100)
gmap.scatter(centroids[:,0],centroids[:,1], 'r', marker=False,size=400)
gmap.draw("Marker.html")

#
# TODO: Repeat the above steps for all 10 individuals, being sure to record their approximate home
# locations. You might want to use a for-loop, unless you enjoy typing.
#
# .. your code here ..


for user in list:
    
    userdata=cdr_df[cdr_df.In==user]

    # INFO: Plot all the call locations
    plottitle='Call locations for user {0}'.format(user)
#    userdata.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title=plottitle)
    
    #toto use gmplot to sdee on map!

#    gmap = gmplot.GoogleMapPlotter(userdata.TowerLat.mean(), userdata.TowerLon.mean(), 10)

#    gmap.scatter(userdata.TowerLat.tolist(), userdata.TowerLon.tolist(), 'r', marker=False)
    userdata=userdata[(userdata.DOW=='Sat') | (userdata.DOW=='Sun')]
    userdata=userdata[(userdata.CallTime<datetime.timedelta(hours=6)) | (userdata.CallTime>=datetime.timedelta(hours=22))]
    
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
    ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)

    #  gmap = gmplot.GoogleMapPlotter(df.Latitude.mean(), df.Longitude.mean(), 10)
    gmap = gmplot.GoogleMapPlotter(newdf.TowerLat.mean(), newdf.TowerLon.mean(), 10)

  
    #gmap.scatter(newdf.TowerLat.tolist(), newdf.TowerLon.tolist(), 'r', marker=False,size=100)
    gmap.scatter(centroids[:,0],centroids[:,1], 'r', marker=False,size=400)
    htmltitle='user_{0}.html'.format(user)
    gmap.draw(htmltitle)

