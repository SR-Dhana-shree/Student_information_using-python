#importing essential modules

from tkinter import*
import tkinter as tk
from time import strftime
from tkinter import ttk
import random
import sqlite3

#making the main window

r=tk.Tk() 
r.title("STUDENT_INFO")
r.geometry('1450x1450')
r.config(bg='skyblue')

#connecting to backend
#create table

conn=sqlite3.connect("stud_info.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS student(
        name text,
        reg_no integer,
        department text,
        email_id text,
        password text)""")

# command for updating a table

def update():
      conn=sqlite3.connect("stud_info.db")
      c=conn.cursor()
      record_id = delete_box.get()
      c.execute("""UPDATE student SET
           name = :name,
           reg_no = :regno,
           department = :dep,
           email_id = :email,
           password = :pwd
            
           WHERE oid = :oid""",
           {
          'name':nameentry_editor.get(),
          'regno':regnoentry_editor.get(),
          'dep':depentry_editor.get(),
          'email':emailentry_editor.get(),
          'pwd':pwdentry_editor.get(),
          'oid':record_id})
      conn.commit()
      conn.close()
      editor.destroy() 

#for making a window for updating

def edit():
     global editor
     editor=tk.Tk()
     editor.title("UPDATE A RECORD")
     editor.geometry('630x450')
     editor.config(bg='orange')
     conn=sqlite3.connect("stud_info.db")
     c=conn.cursor()
     record_id=delete_box.get()
     c.execute("SELECT * FROM student WHERE oid = " + record_id)
     records=c.fetchall()
     global nameentry_editor
     global regnoentry_editor
     global depentry_editor
     global emailentry_editor
     global pwdentry_editor
     L0=tk.Label(editor,text="STUDENT INFORMATION FORM",font=('cambria',30))
     L0.place(x=30,y=50)
     namelbl_editor = tk.Label(editor,text="User Name",font=('cambria', 14))
     namelbl_editor.place(x=135,y=130)
     nameentry_editor = tk.Entry(editor,bd =3)
     nameentry_editor.place(x=280,y=130,width=220,height=25)
     regnolbl_editor = tk.Label(editor,text="Register no",font=('cambria',14))
     regnolbl_editor.place(x=135,y=170)
     regnoentry_editor= tk.Entry(editor,bd =3)
     regnoentry_editor.place(x=280,y=170,width=220,height=25)
     deplbl_editor= tk.Label(editor,text="Department",font=('cambria',14))
     deplbl_editor.place(x=135,y=210)
     depentry_editor = ttk.Combobox(r, width = 27) 
     depentry_editor['values'] = ('CSE','ECE','IT','BCA','B.COM','B.PHARM','TT')
     depentry_editor.place(x=280,y=210,width=220,height=25)
     depentry_editor.current(0)
     depentry_editor = tk.Entry(editor,bd =3)
     depentry_editor.place(x=280,y=210,width=220,height=25)
     emaillbl_editor = tk.Label(editor,text="Email-id",font=('cambria',14))
     emaillbl_editor.place(x=135,y=250)
     emailentry_editor = tk.Entry(editor,bd =3)
     emailentry_editor.place(x=280,y=250,width=220,height=25)
     pwdlbl_editor = tk.Label(editor,text="Password",font=('cambria',14))
     pwdlbl_editor.place(x=135,y=290)
     pwdentry_editor = tk.Entry(editor,show="*",bd =3)
     pwdentry_editor.place(x=280,y=290,width=220,height=25)
     for record in records:
          nameentry_editor.insert(0,record[0])
          regnoentry_editor.insert(0,record[1])
          depentry_editor.insert(0,record[2])
          emailentry_editor.insert(0,record[3])
          pwdentry_editor.insert(0,record[4])
     cancel=Button(editor,text = 'Cancel',bd='5',command = editor.destroy)
     cancel.place(x=190,y=390,width=250,height=28)
     save=Button(editor,text = 'Save Record',bd='5',command = update)
     save.place(x=190,y=350,width=250,height=28)

#for deleting a row in a table

def delete():
     conn=sqlite3.connect("stud_info.db")
     c=conn.cursor()
     c.execute("DELETE FROM student WHERE oid= " + delete_box.get())
     delete_box.delete(0,END)
     conn.commit()
     conn.close()     

#for successfully submit the records (insertion)

def submit():
    conn=sqlite3.connect("stud_info.db")
    c=conn.cursor()
    c.execute("INSERT INTO student VALUES(:E1,:E2,:E3,:E4,:E5)",
              {
                  'E1':name_entry.get(),
                  'E2':reg_entry.get(),
                  'E3':dep_entry.get(),
                  'E4':email_entry.get(),
                  'E5':pwd_entry.get()
              })
    conn.commit()
    conn.close()
    name_entry.delete(0, END)
    reg_entry.delete(0, END)
    dep_entry.delete(0,END)
    email_entry.delete(0, END)
    pwd_entry.delete(0, END)

#To display the content from the table

def query():
    conn=sqlite3.connect("stud_info.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM student")
    records=c.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0])+"\t\t"+str(record[1])+"\t  " +str(record[2])+"\t\t" +str(record[3])+"\t\t\t" +str(record[5])+"\n"
    query_label=Label(r,text = print_records)
    query_label.place(x=650,y=50,width=680,height=600)
    name_lbl_query = tk.Label(r,text="User Name",font=('cambria', 11))
    name_lbl_query.place(x=670,y=55,width=100,height=25)
    reg_lbl_query = tk.Label(r,text="Register no",font=('cambria',11))
    reg_lbl_query.place(x=795,y=55,width=85,height=25)
    dep_lbl_query = tk.Label(r,text="Dep",font=('cambria',11))
    dep_lbl_query.place(x=895,y=55,width=100,height=25)
    email_lbl_query = tk.Label(r,text="Email-id",font=('cambria',11))
    email_lbl_query.place(x=1039,y=55,width=70,height=25)
    oid_lbl_query = tk.Label(r,text="Oid",font=('cambria',11))
    oid_lbl_query.place(x=1245,y=55,width=50,height=25)
    conn.commit()
    conn.close()

#lables for main frames

L0=tk.Label(r,text="STUDENT INFORMATION FORM",font=('cambria',30))
L0.place(x=30,y=50)
name_lbl = tk.Label(r,text="User Name",font=('cambria', 14))
name_lbl.place(x=135,y=130)
name_entry = tk.Entry(r,bd =3)
name_entry.place(x=280,y=130,width=220,height=25)
reg_lbl = tk.Label(r,text="Register no",font=('cambria',14))
reg_lbl.place(x=135,y=170)
reg_entry = tk.Entry(r,bd =3)
reg_entry.place(x=280,y=170,width=220,height=25)
dep_lbl = tk.Label(r,text="Department",font=('cambria',14))
dep_lbl.place(x=135,y=210)
'''dep_entry= ttk.Combobox(r, width = 27) 
dep_entry['values'] = ('CSE','ECE','IT','BCA','B.COM','B.PHARM','TT')
dep_entry.place(x=280,y=210,width=220,height=25)
dep_entry.current(0)'''
dep_entry = tk.Entry(r,bd =3)
dep_entry.place(x=280,y=210,width=220,height=25)
email_lbl = tk.Label(r,text="Email-id",font=('cambria',14))
email_lbl.place(x=135,y=250)
email_entry = tk.Entry(r,bd =3)
email_entry.place(x=280,y=250,width=220,height=25)
pwd_lbl = tk.Label(r,text="Password",font=('cambria',14))
pwd_lbl.place(x=135,y=290)
pwd_entry= tk.Entry(r,show="*",bd =3)
pwd_entry.place(x=280,y=290,width=220,height=25)
cancel=Button(r,text = 'Cancel',bd='5',command = r.destroy)
cancel.place(x=480,y=350,width=80,height=28)
submit=Button(r,text = 'Submit',bd='5',command = submit)
submit.place(x= 380,y=350,width=80,height=28)

#buttons for main frame

query_btn=Button(r,text="Show records",bd='5',command=query)
query_btn.place(x=60,y=350,width=300,height=28)
delete_btn=Button(r,text="Delete records",bd='5',command=delete)
delete_btn.place(x=60,y=460,width=300,height=28)
update_btn=Button(r,text="Update records",bd='5',command=edit)
update_btn.place(x=60,y=500,width=300,height=28)
delete_box = tk.Entry(r,bd=3)
delete_box.place(x=220,y=400,width=150,height=28)
delete_lbl=Label(r,text="Select id",font=('cambria',13))
delete_lbl.place(x=60,y=400,width=150,height=28)

#for about options in menu

def open_about():
    about=Toplevel(r)
    about.geometry("800x300")
    about.config(bg='yellow')
    about.title("About")
    l=Label(about,text='''Developers P.KARPAGALAKSMI & S.R.DHANASHREE
    
    - this is developed using Python tkinter module...
    
    We are collecting students details for our project..''',font=('cambria 18'))
    l.place(x=70,y=40,width=650,height=180) 
    okbtn = Button(about,text='OK',bd='6',command=about.destroy)
    okbtn.place(x=370,y=250,width=60,height=35)
    about.resizable(0,0)
menubar = Menu(r)
file = Menu(menubar,tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File',command = None)
file.add_command(label ='Exit', command = r.destroy)
help_ = Menu(menubar,tearoff = 0)
menubar.add_cascade(label ='About', menu = help_)
help_.add_command(label ='About', command = open_about)
r.config(menu = menubar)

#saving all the operations done in a db-->database

conn.commit()

#closing the connections

conn.close()

# mainloop for getting output

r.mainloop()
