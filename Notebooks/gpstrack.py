import gpxpy
import gpxpy.gpx

gpx_file = open('Morning_Run.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
print gpx.has_times()
print gpx
for track in gpx.tracks:
    for segment in track.segments:
        a=[(x.latitude , x.longitude)  for x in segment.points]
    for segment in track.segments:
        times=[x.time  for x in segment.points]

print times
gpx_file.close()
        
