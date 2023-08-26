#!?usr/bin/python3
"""
Script takes in the name of a state 
as an argument and lists all cities of that state,
using the database hbtn_0e_0.
"""

import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Usage: python 5-filter_cities.py <username> <password> <database> <state>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state = sys.argv[4]

db = MySQLdb.connect(user=username, passwd=password, db=database, port=3306, host="localhost")
cur = db.cursor()

cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC", (state,))
rows = cur.fetchall()

cities = []
for row in rows:
    cities.append(row[0])

print(", ".join(cities))

cur.close()
db.close()