

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

empsal_df = pd.read_csv('empsal.csv', index_col='empno', parse_dates=['dob'])
print(empsal_df.info())

empsal_df.dropna(axis=0, how='any', inplace=True)       
print(empsal_df.info())


empsal_df['spallow']=empsal_df.salary * 0.15
empsal_df['total']= empsal_df.salary + empsal_df.hra + empsal_df.spallow
print(empsal_df.head())




print('Sum Details (M/F):')
print(empsal_df.groupby(['sex'])['salary','hra','spallow','total'].sum())
print('Mean Details (M/F):')
print(empsal_df.groupby(['sex'])['salary','hra','spallow','total'].mean())
print('Standard Deviation Details (M/F):')
print(empsal_df.groupby(['sex'])['salary','hra','spallow','total'].std())

x = input('Press Enter to continue')











