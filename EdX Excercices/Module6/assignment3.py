# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:00:54 2016

@author: paulb
"""

from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC

def doPCA(data, dimensions=2):
#  from sklearn.decomposition import RandomizedPCA
#  model = RandomizedPCA(n_components=dimensions)
  from sklearn.decomposition import PCA
  model = PCA(svd_solver='randomized',n_components=dimensions)

  model.fit(data)
  return model

def doISOMap(data,neighbors=3,ncomponents=3):
    from sklearn import manifold
    iso=manifold.Isomap(n_neighbors=neighbors, n_components=ncomponents)
    iso.fit(data)
    return iso
    
def RunTestData(X_train,y_train,X_test,y_test,identifier):
# vary C from 0.05 to 2.0 in steps of 0.05, and vary
# gamma from 0.001 to 0.1 in steps of 0.001

    best_score=0
    best_c=0
    best_gamma=0
    
    for newC in np.arange(0.05,2.0,0.05) :
         for newgamma in np.arange(0.001,0.1,0.001) :
            model=SVC(C=newC,gamma=newgamma)
            model.fit(X_train,y_train)
            score=model.score(X_test,y_test)
      #      print score
            if score > best_score :
                best_score=score
                best_c=newC
                best_gamma=newgamma
    print "{3} Best setting! C={0}, gamma={1} score={2}".format(best_c,best_gamma,best_score,identifier)
    return best_score,best_c,best_gamma,identifier


dataframe=pd.read_csv("Datasets/parkinsons.data")
dataframe.head(1)
dataframe.dtypes
dataframe.head(1)
X=dataframe.drop('name',axis=1)
X.head(1)
y=X.status
X=X.drop('status',axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=7)

TStanScale = preprocessing.StandardScaler().fit(X_train) #score=0.932203389831
#TMinMax = preprocessing.MinMaxScaler().fit(X_train) #0.881355932203
#TMaxAbs = preprocessing.MaxAbsScaler().fit(X_train) # score=0.881355932203
#TNorm = preprocessing.Normalizer().fit(X_train) #score=0.796610169492
#TKernel = preprocessing.KernelCenterer().fit(X_train) #score=0.915254237288
#T = df # No Change score =0.915254237288


#RunTestData(X_train,y_train,X_test,y_test,"None")
RunTestData(TStanScale.transform(X_train),y_train,TStanScale.transform(X_test),y_test,"TStanScale")
#RunTestData(TMinMax.transform(X_train),y_train,TMinMax.transform(X_test),y_test,"TMinMax")
#RunTestData(TMaxAbs.transform(X_train),y_train,TMaxAbs.transform(X_test),y_test,"TMaxAbs")
#RunTestData(TNorm.transform(X_train),y_train,TNorm.transform(X_test),y_test,"TNorm")
#RunTestData(TKernel.transform(X_train),y_train,TKernel.transform(X_test),y_test,"TKernel")

## best result so far with standardscaled data so use that for the next analysis
X_train=TStanScale.transform(X_train)
X_test=TStanScale.transform(X_test)

#for dims in range(4,15):
#    pcamodel=doPCA(X_train,dims)
#    RunTestData(pcamodel.transform(X_train),y_train,pcamodel.transform(X_test),y_test,"PCA dimensions {0}:".format(dims))

for neighbors in range(2,6):
    for components in range (4,7):
        isomodel=doISOMap(X_train,neighbors,components)
        RunTestData(isomodel.transform(X_train),y_train,isomodel.transform(X_test),y_test,"ISMAp neighbors {0}, components {1}:".format(neighbors,components))


print "done"





      