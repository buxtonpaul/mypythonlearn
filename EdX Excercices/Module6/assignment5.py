import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#
# .. your code here ..

# INFO: An easy way to show which rows have nans in them
#print X[pd.isnull(X).any(axis=1)]
X=pd.read_csv("Datasets/agaricus-lepiota.data",na_values='?')
X=X.dropna(axis=0)

# 
# TODO: Go ahead and drop any row with a nan
#
# .. your code here ..
print X.shape
columns = ["classification","cap-shape",                                 
    "cap-surface",             
    "cap-color",                          
    "bruises?",                
    "odor",                    
    "gill-attachment",         
    "gill-spacing",            
    "gill-size",               
    "gill-color",              
    "stalk-shape",             
    "stalk-root",              
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",  
    "stalk-color-below-ring", 
    "veil-type",               
    "veil-color",              
    "ring-number",             
    "ring-type",
    "spore-print-color",
    "population",              
    "habitat"]

#
# TODO: Copy the labels out of the dset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#
# .. your code here ..


#
# TODO: Encode the entire dataset using dummies
#
# .. your code here ..


# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
# .. your code here ..



#
# TODO: Create an DT classifier. No need to set any parameters
#
# .. your code here ..

 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#
# .. your code here ..
#print "High-Dimensionality Score: ", round((score*100), 3)


#
# TODO: Use the code on the courses SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz. If you can't, use: http://webgraphviz.com/
#
# .. your code here ..


