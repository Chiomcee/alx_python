#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Get states from the database access
    """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE '{}' \
                        ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
