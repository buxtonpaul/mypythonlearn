import pandas as pd
import numpy as np


# Age, is considered continuous although could be ordinal
# education is ordinal,
# gain is continuous
# race is nominal
# capital loss is continuous
# hours per week is continuous
# sex is nominal
# classification is ordinal



#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
# provide a column name for the indices in the data set to make the column easy to drop.
# possible there is a way to drop the column whilst readin....
censusdata=pd.read_csv('census.data',names=['indexnum','education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'],na_values=['?'])
censusdata=censusdata.drop(labels=['indexnum'],axis=1)

#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
ordered_education=['Preschool','1st-4th','5th-6th','7th-8th','9th','10th','11th','12th','HS-grad','Some-college','Bachelors','Masters','Doctorate']

censusdata.education=censusdata.education.astype("category",ordered=True,categories=ordered_education).cat.codes
# astype....cat.codes returns the ordered values of the series, which we then use to replace the original series.

censusdata.classification=censusdata.classification.astype("category",ordered=True,categories=['<=50K','>50K']).cat.codes


#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). Think to yourself, does it generally
# make more sense to have a numeric type or a series of categories
# for these somewhat ambigious features?
#
# .. your code here ..

newdata=pd.get_dummies(censusdata,columns=['race','sex'])
# get_dummies expands out the race and sex columns to provide the binary classiciations for the
# categories that exist. eg. sex_Male, race_Other...


#
# TODO:
# Print out your dataframe
#
# .. your code here ..
print newdata

