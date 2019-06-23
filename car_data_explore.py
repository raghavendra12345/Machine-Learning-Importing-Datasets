# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:38:06 2019

@author: raghu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:46:03 2019

@author: raghu
"""

import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing


car=pd.read_csv("D:\Raghavendra\Machine_Learning_codes\car.data",header=None)
print("The first 2 rows of the automobile dataset is") 
#to print the first 2 rows of datasets
print(car.head(2))
#to print the last 2 rows of datasets
print("The last 2 rows of the automobile dataset is")
print(car.tail(2))
#car.info()

#create a header list as the dataset has no implicit row with headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

car.columns=headers

#to drop missing values from the price column using dropna

car.dropna(subset=["price"], axis=0)

#to find names of the columns
print(car.columns)

#Pandas enables  you to save the dataset to csv by using the dataframe.to_csv()
car.to_csv("automobiles.csv",index=False)


#Exploring the datasets:
#to check the datatypes

print(car.dtypes)

#to get statistical suummary of each of the columns:
print(car.describe())

#to get statistical summary of each of the columns:
#NaN describe not a number 
print(car.describe(include="all"))

#to get summary of only particular column:
print(df[['length','compression-ratio']].describe())

#method to check number of rows and columns in the dataset
print(df.info())