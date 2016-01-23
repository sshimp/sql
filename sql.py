# Create a SQLite3 database and table

import sqlite3

conn = sqlite3.connect("new.db") # creates new database
#conn = sqlite3.connect(":memory:") # would create a memory-only database (not persisted)

cursor = conn.cursor() # creates cursor object to execute SQL commands

cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

conn.close() # close database connection



