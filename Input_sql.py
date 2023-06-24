import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="employee"
)
c = conn.cursor()

# Get user input
slno = int(input("Enter serial number: "))
name = input("Enter name: ")
rollno = int(input("Enter phone number: "))

# Insert data into the table
c.execute("INSERT INTO employee VALUES (%s, %s, %s)", (slno, name, rollno))

# Commit changes and close the connection
conn.commit()
conn.close()
