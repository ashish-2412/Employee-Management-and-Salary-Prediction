# Program name : empmst_proj2.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

empdf = pd.read_csv('empmst.csv', index_col='Empno',parse_dates=['DOB'])
print(empdf)
 
expr = empdf.iloc[:, -3].values    # Pick up experience
salary = empdf.iloc[:,-2].values   # Pick up salary
print('Expr :', expr)
print('Salary ;',salary)

# Draw a scatter plot of Experience vs. Salary
plt.scatter(expr, salary, color = 'red', label='Salary')
plt.title('Salary vs Experience\nScatter Plot')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Find the mean of Salary, HRA, CONV and Total - state wise
empdf['CONV'] = empdf.Salary * 0.1
empdf['Total'] = empdf.Salary + empdf.HRA + empdf.CONV
mean_list = empdf.groupby(['State'])['Salary','HRA','CONV','Total'].mean()
print(mean_list)

# Plotting a bar chart of mean figures of Salary, HRA, CONV, Total
mean_list.plot(kind='bar')
plt.title('State Wise Mean Figures\n Salary, HRA, CONV & Total')
plt.xlabel('States-->')
plt.ylabel('Figures')
plt.tight_layout()
plt.legend(loc='best')
plt.show()
# ---------------------------
# Find the sum,mean,standard deviation of Total, Salary,HRA, CONV gender wise
print('Sum Details (M/F):')
print(empdf.groupby(['Sex'])['Salary','HRA','CONV','Total'].sum())
print('Mean Details (M/F):')
print(empdf.groupby(['Sex'])['Salary','HRA','CONV','Total'].mean())
print('Standard Deviation Details (M/F):')
print(empdf.groupby(['Sex'])['Salary','HRA','CONV','Total'].std())
#------------------------------
# Create a new DF called statewise_total having group by sum() on
# Salary, HRA, CONV, Total
statewise_total = empdf.groupby(['State'])['Salary','HRA', 'CONV','Total'].sum()
print('\n\nDF statewise_total details :')
print(statewise_total)

#-----------------------------------
# Write the new DF with added columns to an Excel file by 'xlwt'
empdf.to_excel('C:\\CSI\\CSI Summer Proj\\CSV XLS files\\empdf.xls')

#----------------------------------------------------------
# Linear Regression Model starts from here
# Reading only Expr and Salary from empmst.csv
print('\n\nMachine Learning starts .....with Linear Regression Model')
emp_expr_sal_df = pd.read_csv('empmst.csv', usecols = ['ExpYr', 'Salary'])
print(emp_expr_sal_df)
X = emp_expr_sal_df.iloc[:, :-1].values # X is Experience. :-1 picks up as 2D
#X = emp_expr_sal_df.iloc[:, -1].values only -1 pick up as 1D array
y = emp_expr_sal_df.iloc[:, 1].values     # y Salary
print(X.shape, type(X))
print(y.shape, type(y))

#Split Train Test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,
                                                    random_state = 0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print('Shape of X_train, y_train :', X_train.shape, y_train.shape)
print('Shape of X_test, y_test :', X_test.shape, y_test.shape)

plt.scatter(expr, salary, color = 'red', label='Salary')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience\nLinear Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary') 
plt.tight_layout()
plt.show()

# Evaluate the model - verify from Test set and find the Test Score
print('Test Score :{:.2f}'.format(regressor.score(X_test, y_test)))

# Prediction. Input years of exp   - independent variable (must be 2D)
# Variable for which prediction to be made must be 2D, so [[ ]]
X_new = np.array([[8.0]])    # 8 years expr
prediction = regressor.predict(X_new)
print('For 8 yrs exp, salary prediction :%.2f' % prediction)
new_expr = float(input('Enter experience in years :'))
new_expr = [[X_new]]       # Convering the input in 2D
prediction = regressor.predict(new_expr)
print('Predicted Salary:%.2f' % prediction)


