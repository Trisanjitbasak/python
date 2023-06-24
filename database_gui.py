import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector

def connect_to_db():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "admin123",
        database = "company_database"
    )
    conn = db.cursor()
    conn.execute("use Company_database;")
    return db, conn

def show_employee_table():
    db, conn = connect_to_db()
    conn.execute("select * from employee")
    data = conn.fetchall()
    table = pd.DataFrame(data, columns=['first_name', 'last_name', 'email_id'])
    print(table)
    db.commit()
    conn.close()
    db.close()

def add_employee():
    db, conn = connect_to_db()
    fname = first_name_entry.get()
    lname = last_name_entry.get()
    email = email_entry.get()
    conn.execute("""INSERT INTO EMPLOYEE VALUES(%s, %s, %s)""",(fname, lname, email))
    db.commit()
    if(conn):
        print("Data restored")
    else:
        print("error occurred")
    conn.close()
    db.close()

def remove_employee():
    db, conn = connect_to_db()
    fname1 = first_name_entry.get()
    conn.execute("""DELETE FROM employee WHERE first_name=%s""",(fname1,))
    db.commit()
    conn.close()
    db.close()

root = tk.Tk()

first_name_label = ttk.Label(root, text="First Name:")
first_name_label.pack()

first_name_entry = ttk.Entry(root)
first_name_entry.pack()

last_name_label = ttk.Label(root, text="Last Name:")
last_name_label.pack()

last_name_entry = ttk.Entry(root)
last_name_entry.pack()

email_label = ttk.Label(root, text="Email:")
email_label.pack()

email_entry = ttk.Entry(root)
email_entry.pack()

show_employee_button = ttk.Button(root, text="Show Employee Table", command=show_employee_table)
show_employee_button.pack()

add_employee_button = ttk.Button(root, text="Add Employee", command=add_employee)
add_employee_button.pack()

remove_employee_button = ttk.Button(root, text="Remove Employee", command=remove_employee)
remove_employee_button.pack()

root.mainloop()
