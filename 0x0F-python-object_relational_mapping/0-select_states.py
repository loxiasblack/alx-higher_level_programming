#!/usr/bin/python3
import MySQLdb
import sys
"""scripts that list all states from database"""

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
