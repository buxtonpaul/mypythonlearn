import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..

servos=pd.read_csv('servo.data',names=['motor','screw','pgain','vgain','class'])

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
vgain5=servos[servos.vgain==5]
print (len(vgain5.index))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..

newslice=servos[(servos.motor=='E') & (servos.screw=='E')]
                
print (len(newslice.index))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
pgainslice=servos[servos.pgain==4]
print(pgainslice.vgain.mean())
# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print(servos.dtypes)



