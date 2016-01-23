# Create a SQLite3 database and table

import sqlite3

conn = sqlite3.connect("new.db") # creates new database
#conn = sqlite3.connect(":memory:") # would create a memory-only database (not persisted)

cursor = conn.cursor() # creates cursor object to execute SQL commands

try:
	cursor.execute("""INSERT INTO population VALUES('Cincinnati','OH',250000)""")  # insert data into table
	cursor.execute("""INSERT INTO population VALUES('Seattle','WA',600000)""")

	conn.commit() # commit changes to database

except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again!"

conn.close() # close database connection



