# Create a SQLite3 database and table

import sqlite3

with sqlite3.connect("new.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	sql = { 'average': "select avg(population) from population", # create dictionary of SQL queries
			'maximum': "select max(population) from population",
			'minimum': "select min(population) from population",
			'sum': "select sum(population) from population",
			'count': "select count(city) from population"
			}

	for key, value in sql.iteritems():

		c.execute(value)

		result = c.fetchone()

		print key + ":", result[0]

#connection.close() # close database connection



