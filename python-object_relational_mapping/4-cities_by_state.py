#!/usr/bin/python3
"""
Script that list all cities from the database
hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute query
    cursor.execute(
            "SELECT cities.id, cities.name, state.name
            FROM cities
            JOIN states ON cities.state_id ORDER BY cities.id ASC")

    # Fetch all rows and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
