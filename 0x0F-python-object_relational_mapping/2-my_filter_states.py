#!/usr/bin/python3
"""script that diplay all states that maches the name argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(sys.argv[4]))
    for name in cursor.fetchall():
        print(name)
    cursor.close()
    db.close()
