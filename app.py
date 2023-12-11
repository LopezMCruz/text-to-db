from dotenv import load_dotenv
import os
import mysql.connector

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# establish connection

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM testtable")

for x in mycursor:
    print(x)