# Add random integers to a new database

import sqlite3

prompt = """
	What aggregation would you like to perform?
	1. Average
	2. Minimum
	3. Maximum
	4. Sum
	5. Exit

	"""

with sqlite3.connect("newnum.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	while True:

		user_input = raw_input(prompt)

		if user_input in set(["1","2","3","4"]):
			operation = {1:"avg",2:"min",3:"max",4:"sum"}[int(user_input)]

			c.execute("select {}(num) from numbers".format(operation))

			result = c.fetchone()

			print "Okay, here is the", \
					{1:"average",2:"minimum",3:"maximum",4:"sum"}[int(user_input)] + "!"
			
			print result[0]

		if user_input == "5":
			print "Exiting..."
			break

#connection.close() # close database connection



