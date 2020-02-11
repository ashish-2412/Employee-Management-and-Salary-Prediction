# Program name : datascience_oper_empmst.py
# Data science operations on empmst.csv

import pandas as pd
import numpy as np
from datetime import datetime

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

empdf = pd.read_csv('empmst.csv', index_col='Empno', parse_dates=['DOB'])
print(empdf.info())
# Drop null values. axis=0 for rowwise drop, axis=1 for col wise.
# 'any' means - drop the row if any col in that row is null
# 'all' means = drop the row if all cols in that row is null 
empdf.dropna(axis=0, how='any', inplace=True)       
print(empdf.info())

# Add columns Conv. Salary
empdf['Conv']=empdf.Salary * 0.30
empdf['Total']= empdf.Salary + empdf.HRA + empdf.Conv
print(empdf.head())

# Calculate Age and add the column 
dt = datetime.today()
age = dt - empdf['DOB']
empdf['Age'] = age/np.timedelta64(1,'Y')    # divide by 'Y' for year. Age comes in float
empdf["Age"] = empdf['Age'].astype(int)     # convert to int

print(empdf.head())

# Write the new DF to a CSV file
empdf.to_csv('c:\\CSI\CSI Summer Proj\\CSV XLS files\\empnew.csv')

# Multiple cols selections
col_lst = ['Empname','Salary']
print(empdf[col_lst])               # or empdf['Empname', 'Salary']
# Select rows with iloc
print(empdf.iloc[:2])               # Top two records
print(empdf.iloc[-2:])              # bottom 2 rows
print(empdf.iloc[:, 0:3])           # All rows with first 3 cols
print(empdf[empdf['Salary'] > 100000])   # Rows with salary > 1L
# AND condition. Rows with Salary > 1L and lives in Kolkata
print(empdf[ (empdf['Salary'] > 100000) & (empdf['City']=='Kolkata')])   
# OR condition.  Rows with Salary > 1L or lives in WB
print(empdf[ (empdf['Salary'] > 100000) | (empdf['State']=='West Bengal')])  

# Rename columns
empdf = empdf.rename(columns={'ExpYr':'Expr'})  # To rename more cols e.g. add 'Salary':'Basic' in { }
print(empdf.head())

# Check for any column/feature having null values or not
print(empdf['DOB'].isnull())        # All should be False as we have removed earlier rows with null values
# Add a column 'marital_stat' and initialized with 0
empdf['marital_stat'] = int(0)
print(empdf.head())
# replace 0 in that field with '-1' just for testing
empdf['marital_stat'].replace(0,-1,inplace=True)
print(empdf.head())

# Find the mean, min, max, median, std deviation of Salary but group by 'State'
print('Mean, min, max, count, median, std of Salary group by State')
print('Mean:\n', empdf['Salary'].groupby(empdf['State']).mean())
print('Min:\n', empdf['Salary'].groupby(empdf['State']).min())
print('Max:\n', empdf['Salary'].groupby(empdf['State']).max())
print('Count :\n',empdf['Salary'].groupby(empdf['State']).count())
print('Median:\n',empdf['Salary'].groupby(empdf['State']).median())
print('Standard Deviation:\n', empdf['Salary'].groupby(empdf['State']).std())
print('Correlation :\n', empdf.corr())

# Sorting rows
print(empdf.sort_values(by='DOB'))      # Ascending
print(empdf.sort_values(by='Salary', ascending=False))   # Descending sort
# Sort on multile fields
print(empdf.sort_values(by=['State', 'City']))
# Convert datatype of a field
empdf['marital_stat'].astype(str, inplace=True)
print(empdf)

# map with DF - map - takes the series and iterate over it
# applymap - applies to each cell/element in the DF
# apply - to apply a function along with the axis
empdf['HRA'] = empdf['HRA'].map(lambda x: x-1000)  # By map/lambda, reduce HRA by 1000 for
                                                   # all employees but
                                                   # to update original DF assign on LHS
print(empdf.head())
# bin categories of Age column and create a new column 'AgeCat'
# Seggregate by Pandas 'cut' method
from sklearn import preprocessing
bins = [20, 30, 40, 50, 60]
group_names = ['20 to 30', '30 to 40', '40 to 50', '50 to 60']
empdf['AgeCat']=pd.cut(empdf['Age'], bins, labels=group_names)
print(empdf.head())











