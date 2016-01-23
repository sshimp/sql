# Add random integers to a new database

import random
import sqlite3


n = [0] * 100

for i in range(100):
	n[i] = (random.randint(0,100),)

with sqlite3.connect("newnum.db") as connection: # connects to existing database ("new.db")
	c = connection.cursor() # creates cursor object to execute SQL commands

	c.execute("create table if not exists numbers (num int)")
	c.executemany("""insert into numbers values(?)""", n)

#connection.close() # close database connection



