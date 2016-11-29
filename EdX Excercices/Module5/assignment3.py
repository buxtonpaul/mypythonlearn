import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
import gmplot
matplotlib.style.use('ggplot') # Look Pretty

#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live at!



def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
#  exit()

def clusterInfo(model):
  print "Cluster Analysis Inertia: ", model.inertia_
  print '------------------------------------------'
  for i in range(len(model.cluster_centers_)):
    print "\n  Cluster ", i
    print "    Centroid ", model.cluster_centers_[i]
    print "    #Samples ", (model.labels_==i).sum() # NumPy Power

# Find the cluster with the least # attached nodes
def clusterWithFewestSamples(model):
  # Ensure there's at least on cluster...
  minSamples = len(model.labels_)
  minCluster = 0
  for i in range(len(model.cluster_centers_)):
    if minSamples > (model.labels_==i).sum():
      minCluster = i
      minSamples = (model.labels_==i).sum()
  print "\n  Cluster With Fewest Samples: ", minCluster
  return (model.labels_==minCluster)


def doKMeans(data, clusters=0):
  #
  # TODO: Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
  # data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
  # no feature scaling is required. Print out the centroid locations and add them onto your scatter
  # plot. Use a distinguishable marker and color.
  #
  # Hint: Make sure you fit ONLY the coordinates, and in the CORRECT order (lat first).
  # This is part of your domain expertise.
  #
  # .. your code here ..
  newdf=data[['TowerLat','TowerLon']]

  model=KMeans(n_clusters=clusters)
  model.fit(newdf)

  return model


  
def HandleUser(userid , cdr):
    user1=cdr_df[cdr_df.In==userid]

    #fig = plt.figure(dpi=200)
    #ax = fig.add_subplot(111)
    #ax.scatter(user1.TowerLon, user1.TowerLat, marker='.', alpha=0.3)
    
    #
    # TODO: Alter your slice so that it includes only Weekday (Mon-Fri) values.
    #
    # .. your code here ..
    
    user1=user1[(user1.DOW!='Sat') & (user1.DOW!='Sun')]
        
    user1.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title='Call Locations')
    #
    # TODO: The idea is that the call was placed before 5pm. From Midnight-730a, the user is
    # probably sleeping and won't call / wake up to take a call. There should be a brief time
    # in the morning during their commute to work, then they'll spend the entire day at work.
    # So the assumption is that most of the time is spent either at work, or in 2nd, at home.
    #
    # .. your code here ..
    user1=user1[(user1.CallTime<=timedelta(hours=17))]       
    ax.scatter(user1.TowerLon, user1.TowerLat, marker='.', alpha=0.3)
    
    #
    # TODO: Plot the Cell Towers the user connected to
    #
    # .. your code here ..
    
    
    
    #
    # INFO: Run K-Means with K=3 or K=4. There really should only be a two areas of concentration. If you
    # notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
    # apart from one another), then increase K=5, with the goal being that all centroids except two will
    # sweep up the annoying outliers and not-home, not-work travel occasions. the other two will zero in
    # on the user's approximate home location and work locations. Or rather the location of the cell
    # tower closest to them.....
    model = doKMeans(user1, 4
                     )
    
    
    #
    # INFO: Print out the mean CallTime value for the samples belonging to the cluster with the LEAST
    # samples attached to it. If our logic is correct, the cluster with the MOST samples will be work.
    # The cluster with the 2nd most samples will be home. And the K=3 cluster with the least samples
    # should be somewhere in between the two. What time, on average, is the user in between home and
    # work, between the midnight and 5pm?
    midWayClusterIndices = clusterWithFewestSamples(model)
    midWaySamples = user1[midWayClusterIndices]
    print "    Its Waypoint Time: ", midWaySamples.CallTime.mean()
    
    
    #
    # Let's visualize the results!
    # First draw the X's for the clusters:
    #ax.scatter(model.cluster_centers_[:,1], model.cluster_centers_[:,0], s=169, c='r', marker='x', alpha=0.8, linewidths=2)
    
    #ax.scatter(model.cluster_centers_[0,1], model.cluster_centers_[0,0], s=169, c='k', marker='x', alpha=0.8, linewidths=2)
    #ax.scatter(model.cluster_centers_[1,1], model.cluster_centers_[1,0], s=169, c='b', marker='x', alpha=0.8, linewidths=2)
    
    gmap = gmplot.GoogleMapPlotter(user1.TowerLat.mean(), user1.TowerLon.mean(), 15)
    
      
    #gmap.scatter(newdf.TowerLat.tolist(), newdf.TowerLon.tolist(), 'r', marker=False,size=100)
    gmap.scatter(model.cluster_centers_[1:2,0],model.cluster_centers_[1:2,1], 'b', marker=False,size=400)
    gmap.scatter(model.cluster_centers_[0:1,0],model.cluster_centers_[0:1,1], 'k', marker=False,size=400)
    htmltitle='user_{0}_home_work.html'.format(userid)
    gmap.draw(htmltitle)

  

#
# TODO: Load up the dataset and take a peek at its head and dtypes.
# Convert the date using pd.to_datetime, and the time using pd.to_timedelta
#
# .. your code here ..


cdr_df=pd.read_csv("Datasets/CDR.csv")
cdr_df.head()
cdr_df.dtypes



#
# TODO: Get a distinct list of "In" phone numbers (users) and store the values in a
# regular python list.
# Hint: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
#
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
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above
#
# .. your code here ..




#
# Then save the results:
#showandtell('Weekday Calls Centroids')  # Comment this line out when you're ready to proceed

for usernum in list:
    print "\n\nExamining person: ", usernum
    HandleUser(usernum,cdr_df)




