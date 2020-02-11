

from   tkinter import *
from   tkinter import messagebox as msg
import sys
import pandas as pd
import mysql.connector as mysql
import os.path
import csv
from tkintertable import TableCanvas 

class create_csv:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()   
           
          
          self.message_label = Label(self.f,text='Convert MySQL data to CSV',font=('Arial', 14))
          
          
          self.confirm_button = Button(self.f,text='Convert', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_csv)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     
     def conv_to_csv(self):
         
         try:
             conn = mysql.connect(user='ashish',password='ashish2412', host='127.0.0.1', database='hr')
             
             if( conn.is_connected()):
                    msg.showinfo('Connected to MySQL Database', 'Connected to MySQL DB')
             else:
                    msg.showerror('Error connecting Database', 'Error in connecting MySQL')
    
             cur = conn.cursor()
              
             if(os.path.exists('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/empsal.csv')):
                os.remove('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/empsal.csv')    
 
             str = "select * from empsal into outfile 'c:/ProgramData/MySQL/MySQL Server 8.0/Uploads/empsal.csv' \
                    fields terminated by ',' lines terminated by '\r\n'"  

             cur.execute(str)         
             if (cur.rowcount) == 0:
                    msg.showinfo('No records', 'No records')
             else:
                    msg.showinfo('CSV file created', 'CSV file created')
             
             
             df = pd.read_csv('c:/ProgramData/MySQL/MySQL Server 8.0/Uploads/empsal.csv')
             df.to_csv('D:/Training_project/Project3/csv_created/empsal.csv', index=False)

              
             with open('D:/Training_project/Project3/csv_created/empsal.csv',newline='') as f:
                  r = csv.reader(f)
                  data = [line for line in r]          
                  
             with open('empsal.csv','w',newline='') as f:
                  w = csv.writer(f)
                  w.writerow(['empno','empname','dob','sex','city','state','expyr','salary','hra'])  
                  w.writerows(data)              
                      
             
             self.f = Frame(root, height=200, width=300) 
             self.f.pack(fill=BOTH,expand=1)
             self.table = TableCanvas(self.f, read_only=True)
             self.table.importCSV('empsal.csv')
             
             self.table.show()
        
         except  mysql.Error as e:
             msg.showerror('Error in executing DB commands', e.msg)
         finally:
             cur.close()
             conn.close()

root=Tk()
root.title('Conversion of MySQL data to CSV')
root.geometry('800x600')
conv_csv = create_csv(root)
root.mainloop()

