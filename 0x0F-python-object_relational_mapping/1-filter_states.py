#!/usr/bin/python3
"""scritpts that select from a name all name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
