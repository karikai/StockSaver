import mysql.connector

## Your password for the mySQL
password = ''

## Connects to mySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password
)

myCursor = mydb.cursor()

myCursor.execute("CREATE DATABASE stocks;")

myCursor.execute("USE stocks;")

myCursor.execute("CREATE TABLE symbols (symbolName VARCHAR(255));")