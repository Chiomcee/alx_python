#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connection to database server
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Cursor object creation
    cursor = db.cursor()

    # Query execution
    cursor.execute(
            "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    # Results printing
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
