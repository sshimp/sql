# Create a SQLite3 database and table

import sqlite3

conn = sqlite3.connect("cars.db") # creates new database
#conn = sqlite3.connect(":memory:") # would create a memory-only database (not persisted)

cursor = conn.cursor() # creates cursor object to execute SQL commands

cursor.execute("""CREATE TABLE inventory (Make TEXT, Model TEXT, Quantity INT)""")

conn.close() # close database connection



