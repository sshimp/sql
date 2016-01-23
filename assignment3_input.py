# Add random integers to a new database

import sqlite3

user_input = raw_input("What aggregation would you like to perform?")

print "Okay, here is the", user_input + "!"

sql = { 'average': "select avg(num) from numbers", # create dictionary of SQL queries
		'maximum': "select max(num) from numbers",
		'minimum': "select min(num) from numbers",
		'sum': "select sum(num) from numbers",
		}

with sqlite3.connect("newnum.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	c.execute(sql[user_input])

	result = c.fetchone()

	print result[0]

#connection.close() # close database connection



