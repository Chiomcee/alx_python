#!/usr/bin/python3
"""
    This script takes in an argument and displays all values i
    n the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()
