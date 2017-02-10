 p4 changes //powervr/swvideo/projects/felix/MAIN... >somefile.log
 python acc_changes.py -o outputlog.log somefile.log
 python p4-gource.py  -o main.gource outputlog.log 
 gource main.gource -s 0.0005 --max-files 100
 #gource main.gource -s 0.00005 --hide filenames,dirnames -o gource.ppm
 #ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i gource.ppm -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4
 