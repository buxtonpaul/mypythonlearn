# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:46:54 2016

@author: paul.buxton
"""

import gpxpy
import gpxpy.gpx

from haversine import haversine


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import gmplot


#gpx_file = open('gps_export_20161009_0755.gpx', 'r')
gpx_file = open('Club_Fartlek.gpx', 'r')
#gpx_file = open('Morning_Run.gpx', 'r')
#gpx_file = open('validation_gpx10.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
gpx_file.close()
#print gpx

# arrays to hold complete track info
cum_dist=[]
speed=[]
delta_distance=[]
delta_time=[]
cum_time=[]
mpm=[]
for track in gpx.tracks:
    for segment in track.segments:
        times=[x.time  for x in segment.points]
    for segment in track.segments:
        # set the starting pos
        prev_pos=(segment.points[0].latitude,segment.points[0].latitude)
#        coords=[(x.latitude , x.longitude)  for x in segment.points]
        lats=[x.latitude for x in segment.points]
        longs=[x.longitude for x in segment.points]
        n=0
        
        prev_pos=(lats[0],longs[0])
        prev_time=times[0]
        for x in segment.points:
            delta_distance.append(haversine(prev_pos,(lats[n],longs[n])))
            # possibly want to add eleveations....
            delta_time.append((times[n]-prev_time).total_seconds())
            
            cum_dist.append(sum(delta_distance))
            cum_time.append(sum(delta_time))
            #avoid /0 errors
            if(delta_time[n]==0):
                speed.append(0)
            else:
                speed.append((delta_distance[n]*1000.0)/delta_time[n])
            # avoid /0 errors
            if(speed[n]==0):
                mpm.append(0)
            else:
                mpm.append(1/(speed[n]*0.03728227153424))

            prev_pos=(lats[n],longs[n])
            prev_time=times[n]
            n=n+1
            
            

totaldistance=sum(delta_distance)
print "Distance covered %fkm %f miles" % (totaldistance,totaldistance /1.609)

#print delta_distance
#print speed
#print mpm
# fix maths here


figure()
plot(cum_time, mpm, 'r')
xlabel('Time in s')
ylabel('pace in mins per mile')
yticks([4,5,6,7,8,9,10,11,12,13,14,15])
title('Pace in M/Mile')
ylim([0,15])
show()



#figure()

#plot(cum_time, speed, 'r')
#xlabel('Time in s')
#ylabel('Speed in m/s')
#title('Speed in M/s')
#show()




gmap = gmplot.GoogleMapPlotter(mean(lats), mean(longs), 16)

  
#gmap.scatter(newdf.TowerLat.tolist(), newdf.TowerLon.tolist(), 'r', marker=False,size=100)
gmap.plot(lats,longs, 'r', marker=False,size=400)
htmltitle='run.html'
gmap.draw(htmltitle)


