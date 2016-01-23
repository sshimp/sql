# Create a SQLite3 database and table

import sqlite3

with sqlite3.connect("new.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	c.execute("""
		SELECT DISTINCT population.city, population.population, region.region 
		from population, region
		where population.city = region.city
		ORDER BY population.population DESC
		""")

	rows = c.fetchall()

	for r in rows:
		print "City: " + r[0]
		print "Population: " + str(r[1]) # convert integer to string
		print "Region: " + r[2]
		print "-----------"

#connection.close() # close database connection



