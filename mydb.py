import mysql.connector
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

dataBase = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done !!")


