#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Safe from MySQL injections.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute parameterized query
    cursor.execute(
            "SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (argv[4],))

    # Fetch all rows and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
