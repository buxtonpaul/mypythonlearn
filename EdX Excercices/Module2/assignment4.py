import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
nhlpps=pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2',header=1)


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
rankings=nhlpps[0]
rankings.columns=['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM',
       'PTS/G', 'SOG', 'PCT', 'GWG', 'PPG', 'PPA', 'SHG', 'SHA']
       
# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
rankings=rankings.dropna(axis=0,thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
rankings=rankings[rankings.PLAYER!='PLAYER']

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
rankings=rankings.drop(labels=['RK'],axis=1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
rankings=rankings.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

rankings.loc[:,'GP']=pd.to_numeric(rankings.loc[:,'GP'],errors='coerce')
rankings.loc[:,'G']=pd.to_numeric(rankings.loc[:,'G'],errors='coerce')
rankings.loc[:,'A']=pd.to_numeric(rankings.loc[:,'A'],errors='coerce')
rankings.loc[:,'PTS']=pd.to_numeric(rankings.loc[:,'PTS'],errors='coerce')
rankings.loc[:,'PIM']=pd.to_numeric(rankings.loc[:,'PIM'],errors='coerce')
rankings.loc[:,'PTS/G']=pd.to_numeric(rankings.loc[:,'PTS/G'],errors='coerce')
rankings.loc[:,'SOG']=pd.to_numeric(rankings.loc[:,'SOG'],errors='coerce')
rankings.loc[:,'PCT']=pd.to_numeric(rankings.loc[:,'PCT'],errors='coerce')
rankings.loc[:,'GWG']=pd.to_numeric(rankings.loc[:,'GWG'],errors='coerce')
rankings.loc[:,'PPG']=pd.to_numeric(rankings.loc[:,'PPG'],errors='coerce')
rankings.loc[:,'PPA']=pd.to_numeric(rankings.loc[:,'PPA'],errors='coerce')
rankings.loc[:,'SHG']=pd.to_numeric(rankings.loc[:,'SHG'],errors='coerce')
rankings.loc[:,'SHA']=pd.to_numeric(rankings.loc[:,'SHA'],errors='coerce')
## how to handle the ones with the dodgy name
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print(rankings)

print 'Entries = %d' % len(rankings.index)

print 'Unique PCT %d ' % len(rankings.PCT.unique())
print 'Sum of GP for entries 15 and 16 %d' % sum(rankings.loc[15:16,'GP'])
