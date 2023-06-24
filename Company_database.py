import pandas as pd
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin123",
    database = "company_database"
)
conn = db.cursor()
conn.execute("use Company_database;")
print("Enter 1 to see/modify employee table")
print("Enter 2 to see/modify branch table")
a = int(input())
while True:
    fname=0
    if(a == 1):
        print("Enter 1 to see employee table")
        print("Enter 2 to modify employee table")
        print("Enter 3 to exit to main menu")
        b = int(input())
        if(b == 1):
            conn.execute("select * from employee")
            data = conn.fetchall()
            table = pd.DataFrame(data, columns=['first_name', 'last_name', 'email_id'])
            print(table)
            db.commit()
        elif(b == 2):
            while True:
                print("Enter 1 to add employee")
                print("Enter 2 to remove employee")
                print("Enter 3 to exit to main menu")
                c = int(input())
                if(c == 1):
                    print("Enter the first_name")
                    fname = input()
                    print("Enter the last_name")
                    lname = input()
                    print("Enter the email_id")
                    email = input()
                    conn.execute("""INSERT INTO EMPLOYEE VALUES(%s, %s, %s)""",(fname, lname, email))
                    db.commit()
                    if(conn):
                        print("Data restored")
                    else:
                        print("error occurred")    
                elif(c == 2):
                    fname1 = input("Enter the name of the employee to be removed")
                    conn.execute("""DELETE FROM employee WHERE first_name=%s""",(fname1,))
                    db.commit()
                elif(c == 3):
                    break;
        elif(b == 3):
            break;        
    elif(a == 2):
        print("Enter 1 to see branch table")
        print("Enter 2 to modify branch table")
        print("Enter 3 to exit to main menu")
        d = int(input())
        if(d == 1):
            conn.execute("select * from branch")
            data = conn.fetchall()
            table = pd.DataFrame(data, columns=['branch_code', 'district', 'city', 'state'])
            print(table)
            db.commit()
        elif(d == 2):
            while True:
                print("Enter 1 to add branch")
                print("Enter 2 to remove branch")
                print("Enter 3 to exit to main menu")
                e = int(input())
                if(e == 1):
                    print("Enter the branch_code")
                    bcode = int(input())
                    print("Enter the district")
                    district = input()
                    print("Enter the city")
                    city = input()
                    print("Enter the state")
                    state = input()
                    conn.execute("""INSERT INTO BRANCH VALUES(%s, %s, %s, %s)""",(bcode, district, city, state))
                    db.commit()
                    if(conn):
                        print("Data restored")
                    else:
                        print("error occurred")    
                elif(e == 2):
                    bcode1 = input("Enter the name of the branch_code of the branch to be removed")
                    conn.execute("""DELETE FROM branch WHERE branch_code=%s""",(bcode1,))
                    db.commit()
                elif(e == 3):
                    break;
        elif(d == 3):
            break;
    elif(a == 3):
        break;        
conn.close()
db.close()                
