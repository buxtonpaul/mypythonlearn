
source = 'level'
seperated=list(source)
seperated.reverse()
revstring=''.join(seperated)
print revstring == source


#alternative using slicing and stride
print(source==source[::-1])
