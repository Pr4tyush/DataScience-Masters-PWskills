import mysql.connector
#connection String
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "manager"
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASE;")
for x in mycursor:
    print(x)