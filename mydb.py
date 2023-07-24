# pip install mysql-connector
import mysql.connector

dataBase = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     passwd = 'SudokuRoot',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sudukodb")

dataBase.commit()  # Commit the changes to make them permanent.

print("All Done!!")