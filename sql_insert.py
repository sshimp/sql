# Create a SQLite3 database and table

import sqlite3

with sqlite3.connect("new.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	cities = [ # create python list of rows to be inserted
			('Boston', 'MA', 600000),
			('Los Angeles', 'CA', 38000000),
			('Houston', 'TX', 2100000),
			('Philadelphia', 'PA', 1500000),
			('San Antonio', 'TX', 1400000),
			('San Diego', 'CA', 130000),
			('Dallas', 'TX', 1200000),
			('San Jose', 'CA', 900000),
			('Jacksonville', 'FL', 800000),
			('Indianapolis', 'IN', 800000),
			('Austin', 'TX', 800000),
			('Detroit', 'MI', 700000)
		 	]

	c.execute("""CREATE TABLE IF NOT EXISTS population (city TEXT, state TEXT, population INT)""")
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities) # insert entire list

#connection.close() # close database connection



