import mysql.connector
#import MySQLdb

#Create Connection
conn=mysql.connector.connect(host="localhost",user="root",passwd="ceit")

#Create cursor object
MYCURSOR=conn.cursor()

#MYCURSOR.execute("CREATE DATABASE buklibrary")
MYCURSOR.execute("USE buklibrary")

#Create table
tablebooks= """CREATE TABLE Books(BookID int primary key,Title varchar(20),Author varchar(20),Genre varchar(20))"""

#MYCURSOR.execute(tablebooks)

#Insert Value into table
#Insertvalue= """INSERT INTO Books VALUES(101,"Days of the Week","Joe Blue","Education")"""
Insertvalue2="""INSERT INTO Books VALUES(102,"Fall Of Giants","Ken Follet","History")"""
#MYCURSOR.execute(Insertvalue)
MYCURSOR.execute(Insertvalue2)

#Viewing
MYCURSOR.execute("SELECT * FROM Books")
result= MYCURSOR.fetchall()
conn.commit()

for row in result:
    print(row)
    print("\n")