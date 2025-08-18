import mysql.connector;

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='85d70dde01e2e33496c0f186cd77a6ee0b34423b3c26a74fda8eecdb21d091e4'
)

# cursor object

cursorObject=dataBase.cursor()

#create DB

cursorObject.execute("CREATE DATABASE elderco")

print("All Done  !!") # only for testing that the code is working fine


