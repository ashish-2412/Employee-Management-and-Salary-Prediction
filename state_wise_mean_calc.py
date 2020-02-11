
import pandas as pd
import matplotlib.pyplot as plt

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
mean_list = empsal_df.groupby(['state'])['salary','hra','spallow','total'].mean()
print(mean_list)


mean_list.plot(kind='bar')
plt.title('State Wise Mean Figures Of\n salary, hra, conv & total')
plt.xlabel('States-->')
plt.ylabel('Mean Figures')
plt.tight_layout()
plt.legend(loc='best')
plt.show()

x = input('Press Enter to continue')











