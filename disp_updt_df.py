

from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
import mysql.connector as mysql

from pandastable import Table

class create_df:
       def __init__(self, root):
              self.f = Frame(root, height=350, width=500)
              self.f.pack()    
              
              
              self.message_label = Label(self.f,text='Display the updated DF with Sp allowance and total',font=('Arial', 14))
              
              
              self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                   fg='Black', command=self.conv_to_df)
              self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                   fg='Black', command=root.destroy)

              
              self.message_label.grid(row=1, column=0)
              self.confirm_button.grid(row=2,column=0)
              self.exit_button.grid(row=2,column=2)
       
       def conv_to_df(self):

              
              try:
                     conn = mysql.connect(user='ashish',password='ashish2412', host='127.0.0.1', database='hr')
              
                     if( conn.is_connected()):
                            msg.showinfo('Connected to MySQL Database', 'Connected to MySQL DB')
                     else:
                            msg.showerror('Error connecting Database', 'Error in connecting MySQL')

                     empsal_df = pd.read_sql("select * from empsal", conn, index_col='empno')
              

              
                     empsal_df['spallow'] = empsal_df.salary * 0.15
                     empsal_df['total']= empsal_df.salary + empsal_df.hra + empsal_df.spallow
                     
                     if (len(empsal_df)== 0):
                            msg.showinfo('No records', 'No records')
                     else:
                            msg.showinfo('Pandas DF created', 'Pandas DF created')
                            
                     
                     
                     self.f = Frame(root, height=200, width=300) 
                     self.f.pack(fill=BOTH,expand=1)
                     self.table = Table(self.f, dataframe=empsal_df,read_only=True)
                     self.table.show()
              
              except  mysql.Error as e:
                     msg.showerror('Error in executing DB commands', e.msg)
              finally:
                     conn.close()
             

root=Tk()
root.title('Display the updated DF with Sp allowance and total')
root.geometry('800x600')
conv_csv = create_df(root)
root.mainloop()

