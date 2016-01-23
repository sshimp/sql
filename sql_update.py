# Create a SQLite3 database and table

import sqlite3
import csv

with sqlite3.connect("new.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	c.execute("""UPDATE population SET population = 9000000 WHERE city = 'New York City'""")
	c.execute("""DELETE FROM population WHERE city = 'Boston'""")

	print "\nNEW DATA\n"

	c.execute("""SELECT * FROM population""")

	rows = c.fetchall()

	for r in rows:
		print r[0],r[2]

#connection.close() # close database connection



