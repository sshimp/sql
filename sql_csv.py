# Create a SQLite3 database and table

import sqlite3
import csv

with sqlite3.connect("csv.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	employees = csv.reader(open("employees.csv","rU"))

	c.execute("""CREATE TABLE IF NOT EXISTS employees (firstname TEXT, lastname TEXT)""")
	c.executemany('INSERT INTO employees VALUES(?, ?)', employees) # insert entire list

#connection.close() # close database connection



