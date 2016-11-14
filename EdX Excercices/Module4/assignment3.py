import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper
import numpy as np
from sklearn.decomposition import PCA

# Look pretty...
matplotlib.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
scaleFeatures = True


# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
# .. your code here ..

kidneys=pd.read_csv('Datasets/kidney_disease.csv')
kidneys=kidneys.dropna(axis=0)
kidneys=kidneys.reset_index()


# call the pd.to_numeric function on all the values in columd=s rc and wc

# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['red' if i=='ckd' else 'green' for i in kidneys.classification]



#df=kidneys.drop(labels=['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'],axis=1)
df=kidneys.drop(labels=['id', 'classification'],axis=1)
df=pd.get_dummies(df,columns=['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'])
print df.dtypes

#df=df.apply(pd.to_numeric,errors='coerce')
df[['pcv','wc','rc']]=df[['pcv','wc','rc']].apply(pd.to_numeric,errors='coerce')
print df.dtypes
df.describe()
print df.var(axis=0)


# TODO: This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
if scaleFeatures: df = helper.scaleFeatures(df)

pca=PCA(n_components=2)
pca.fit(df)
      
T=pca.transform(df)


# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
# .. your code here ..


# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
#ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
#T.head()
#T.describe()
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, )
plt.show()


