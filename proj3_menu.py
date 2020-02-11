from tkinter import *
import sys
import os
import subprocess

class Empsal:

    
    def __init__(self, root):

        self.main_lbl=Label(root, text='Employee HR Database Management System', fg='black', font=('Arial', -20, 'bold'))
        self.main_lbl.place(x=190, y=250)
       
        
        self.menubar=Menu(root)
        root.config(menu=self.menubar)           
        
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='CSV/DF File Maintenance', menu=self.mysql_menu)
        
        self.mysql_menu.add_command(label='Build / Display CSV File', command=self.create_csv)
        self.mysql_menu.add_command(label='Build / Display Pandas DF', command=self.create_df)
         
        
        self.mysql_menu.add_separator()
        
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        
        self.reports_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports/Data Visualization', menu=self.reports_menu)

        self.reports_menu.add_command(label='Display Updated DF', command=self.disp_updt_df)
        self.reports_menu.add_command(label='Gender Wise Sum, Mean, Std. Deviation', command=self.gender_wise_calc)
        self.reports_menu.add_command(label='State Wise Mean Expenses, Bar Graph', command=self.state_wise_mean_calc)
        self.reports_menu.add_command(label='State Wise Total Expenses, Bar Graph', command=self.state_wise_total_calc)
        self.reports_menu.add_command(label='Scatter Plot - Experience(X), Salary(Y)', command=self.scatter_plot)

        
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict Salary (Given Experience)', command=self.predict_salary)
         
    def create_csv(self):
        os.system("python D:\Training_project\Project3\create_csv.py")
    def create_df(self):
        os.system("python D:\Training_project\Project3\create_df.py") 

    def disp_updt_df(self):
        os.system("python D:\Training_project\Project3\disp_updt_df.py")
    def gender_wise_calc(self):
        os.system("python D:\Training_project\Project3\gender_wise_calc.py")  
    def state_wise_mean_calc(self):
        os.system("python D:\Training_project\Project3\state_wise_mean_calc.py")
    def state_wise_total_calc(self):
        os.system("python D:\Training_project\Project3\state_wise_total_calc.py")
    def scatter_plot(self):
        os.system("python D:\Training_project\Project3\scatter_plot.py")

    def predict_salary(self):
        os.system("python D:\Training_project\Project3\predict_salary.py")

  
root=Tk()
root.configure(background='white')
root.title('Employee HR Database Query using Python Data Science Tool(Pandas)')

obj=Empsal(root)
root.geometry('800x600')
root.mainloop()

                                 
        
        
        
        
                 
