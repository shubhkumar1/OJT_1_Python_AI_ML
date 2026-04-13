import mysql.connector
myDb = mysql.connector.connect(host="127.0.0.0",user="root",passwd="",database="Python_OJT")
str1 = "Insert into Student values('Shubham', 'BCA', '23MCR121', '12-Jan-2005')"
my = myDb.cursor()
my.execute(str1)
myDb.commit()
print("Done Baby")