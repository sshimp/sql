# Create a SQLite3 database and table

import sqlite3

conn = sqlite3.connect("new.db") # creates new database
#conn = sqlite3.connect(":memory:") # would create a memory-only database (not persisted)

cursor = conn.cursor() # creates cursor object to execute SQL commands

cursor.execute("""INSERT INTO population VALUES('New York City','NY',8200000)""")  # insert data into table
cursor.execute("""INSERT INTO population VALUES('San Francisco','CA',800000)""")

conn.commit() # commit changes to database

conn.close() # close database connection



