# Create a SQLite3 database and table

import sqlite3
import csv

with sqlite3.connect("csv.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	c.execute("""SELECT firstname, lastname from employees""") # execute query on table
	rows = c.fetchall() # return all records from query as list of tuples

	for r in rows: 
		print r[0], r[1] # print all records in a loop

#connection.close() # close database connection



