# Library numpy and funcitonalities

# numpy utilizes the homogeneous array data type to create and manipulate matrices
import numpy as np

x = np.arange(36).reshape(6,6) # Generates the numbers 0-35, arranges them in a 6x6 matrix
x = np.arange(216).reshape(6,6,6) # Generates the numbers from 0-215, arranges them in a 6x6x6 3 dimensional matrix
x                              # displays the value of x 
print(x)

x.ndim # returns the number of dimensions in the array

x = np.arange(21).reshape(3,7) # generates the numbers 0-20, arranges them in a 3x7 matrix

x

# arithmetic operations in numpy
y = np.arange(5,26).reshape(3,7) # generates numbers 5-25, arranges them in a 3x7 array
y

z = x+y
z                               # returns the matrix addition of x and y

z = 10*z
z                               # scalar mulitpilication of z by 10

z = x*y
z                               # item by item mulitplication of x and y

z = x@y 
z                               # matrix multiplication of x and y. This must return an error

y = np.arange(5,26).reshape(7,3) # for matrix multiplication, we need matrices such that no. of columns of y = no.of rows of x
z = x@y
z                               # matrix product of a 3x7 and a 7x3 matrix would be a 3X3 matrix

z.T                      # transposed matrix of z , converts rows to columns and columns to rows

a = np.ones((2,3),dtype =int) # creates an array containing all values as 1
a

a*=3                    # using the operands to multiply the array a by 3 and storing the value inside
a

b = np.random.random((2,3)) # Create another array of 2x3 dimensions containing random values
b

b += a                  # Using the operands to add a and b and store the values in b
b

#Generate random set of normal variables and create a visualization

import numpy as np  
import matplotlib.pyplot as plt # calling the matplotlib library for visualization needs
# naming matplotlib instance as plt is a general convention. 

mean = 20
sd = 3
dist = np.random.normal(mean,sd,10000) # create an object containing 10000 values of a normal distribution of mean 20 and standard deviation 3

plt.hist(dist, bins=100, density =1, color ='green') # plots the normal distribution in a green color and solid density
plt.show 
################################################################################
################################################################################

#import external csv files into python and doing analysis on it

file = open('Sales_data.csv','r')
file.read()
file.close()
# import csv files using pandas library and do data manipulation on the dataset

import pandas as pd # imports the library of pandas and stores in the object pd.

# naming the class as pd is a general convention

df = pd.read_csv('Sales_data.csv', sep=',', header=0) # imports external csv data set from file explorer 
print(df) 
print(df.head(5))       # returns the first 5 rows
print(df.tail(5))       # returns the last 5 rows
print(df.columns)       # returns an array containing the names of the columns

# loc, iloc and 
# loc function allows users to retrieve subsets of data by specific rows and columns
df.loc[:,['order_no','order_qty']]      # :returns all rows and columns order_no and order_qty
df.loc[3:97:,'order_no':'sales']        # returns the rows from 3rd to 97th and the columns order_no and sales
df.loc[3:97 , 3:4] # returns error because loc doesn't identify columns by number

# iloc on the other hand allows users to retrieve subsets of data by specif rows and columsn by number
df.iloc[4:97,[3,5,8]]                   # returns a subset of rows from 4-97 and columns 3,5 and 8
print(df.iloc[4:25:,3:7])               # returns a subset of rows from 4-25 and columns 3 through 7



print(df.describe)                      # returns a list of statistical summary of the data set
df_sort = df.sort_values('order_qty', ascending = 'false') # when ascending =false, the sort is done as descending order
df_sort


################################################################################

# Data cleaning and validation using pandas
# Pandas sits on numpy and utilises all the functions and techniques from numpy

import pandas as pd
df = pd.read_csv("Sales_data.csv")

df.head()
df.columns
df.describe

df.columns = df.columns.str.upper()     # converts the header names to all caps and returns an array


df.rename(columns = {'SALES':'REVENUE'})# allows users to change the names of the headers
df.columns


# null values or missing values can be treated using multiple strategies
# null values can be replaced with a nuetral value such as zero or replaced with an average of the variable
# null values also can be dropped from the dataset if the values aren't too many
# these strategies need to be assessed and decided upon by the user


df.isnull()                             # returns an array of boolean variables by identifying null values. 
                                        # if the cell contains a null value a True value is returned
df.isnull().any()                       # returns the number of missing values or nulls under each header
df.isnull().sum().sum()                 # returns the total number of missing values in the dataset

df_replace_0 = df.fillna(0)             # replaces the missing values with 0
df_replace_0                            
df_replace_0.isnull()                   # Now the missing values have been replaced with 0
df_replace_0.isnull().any()             # Hence the values have changed to False for all headers

df = df_replace_0

df_replace_mean = df.SALES.fillna(df.SALES.mean()) # Allows users to replace missing values with the average value of the vector
df.SALES = df_replace_mean
df

df = pd.read_csv('Sales_data.csv')

df.isnull().any()
df.shape

df_drop_na = df.dropna()                # drops the rows containing null values
df_drop_na
df_drop_na.shape

df_drop_order_no = df.drop(['order_no'], axis = 1 )
df_drop_order_no.columns

##############################################################################
##############################################################################

#Merging datasets using Pandas
#Datasets containing similar data but from different sources or time stamps can be merged using pandas
#Datasets can be merged by various strategies depending upon the required need of the analysis exercise
#Merging can be done based on one or more IDs or key values. 
#They can also be joined as an intersection or as a union using inner and outer joins

import pandas as pd
x = pd.read_csv('fruit_a.csv')
y = pd.read_csv('fruit_b.csv')

# the dataset contains two similar datasets of fruit information, containing variables such as price, seasonal, on sale and vitamins
# we wish to get either intersections or unions of data. Not all fruits will have all the information.

print(x)
print(y)

merge_key = pd.merge(x,y, on = 'ID')
print(merge_key)

left_merge =  pd.merge(x, y, on='ID', how='left') # returns a left join
print(left_merge)

right_merge = pd.merge(x,y, on='ID', how = 'right' ) # returns a right join
print(right_merge)

inner_merge = pd.merge(x,y, on = 'ID', how = 'inner') # returns an inner join

outer_merge = pd.merge(x,y, on = 'ID', how ='outer') # returns an outer join

print(inner_merge)
print(outer_merge)

