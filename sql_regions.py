# Create a SQLite3 database and table

import sqlite3

with sqlite3.connect("new.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	cities = [ # create python list of rows to be inserted
			('New York City', 'Northeast'),
			('San Francisco', 'West'),
			('Chicago', 'Midwest'),
			('Houston', 'South'),
			('Phoenix', 'West'),
			('Boston', 'Northeast'),
			('Los Angeles', 'West'),
			('Houston', 'South'),
			('Philadelphia', 'Northeast'),
			('San Antonio', 'South'),
			('San Diego', 'West'),
			('Dallas', 'South'),
			('San Jose', 'West'),
			('Jacksonville', 'South'),
			('Indianapolis', 'Midwest'),
			('Austin', 'South'),
			('Detroit', 'Midwest')
		 	]

	c.execute("""CREATE TABLE IF NOT EXISTS region (city TEXT, region TEXT)""")
	c.executemany('INSERT INTO region VALUES(?, ?)', cities) # insert entire list
	c.execute("""SELECT * FROM region ORDER BY region ASC""")

	rows = c.fetchall()

	for r in rows:
		print r[1], r[0]

#connection.close() # close database connection



