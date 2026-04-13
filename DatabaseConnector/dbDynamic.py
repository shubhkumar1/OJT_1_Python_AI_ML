import mysql.connector as dbc
myDb = dbc.connect(host = "127.0.0.1", user = "root", password = "", database = "Python_OJT")
name = input("Enter your Name - ")
dept = input("Enter your Dept. - ")
roll = input("Enter your Roll No. - ")
dob = input("Enter your DOB - ")

str = "Insert into Student values(" + "'" + name + "'" + "," + "'" + dept + "'" + "," + "'" + roll + "'" + "," + "'" + dob + "'" + ")"

my = myDb.cursor()
my.execute(str)
myDb.commit()
print("\nDone Baby\n")