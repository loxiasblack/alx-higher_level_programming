#!/usr/bin/python3
"""Scripts that displays values that matches the arguments and
safe from SQL injections"""


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
    statename = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s \
                   ORDER BY states.id ASC", (statename,))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
