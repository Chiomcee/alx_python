#!/usr/bin/python3
"""
    List all states from database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SELECT query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the results
    results = cursor.fetchall()

    # Print the results

    for row in results:
        print(row)

    # Close the database connection
    db.close()
