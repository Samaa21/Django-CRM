import mysql.connector;

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Enter Password'
)

# cursor object

cursorObject=dataBase.cursor()

#create DB

cursorObject.execute("CREATE DATABASE elderco")

print("All Done  !!") # only for testing that the code is working fine


