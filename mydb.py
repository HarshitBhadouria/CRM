# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector-python

import mysql
import mysql.connector

dtbase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'

)

cursorObj = dtbase.cursor()

cursorObj.execute("CREATE DATABASE harshitco")

print("All Done!")