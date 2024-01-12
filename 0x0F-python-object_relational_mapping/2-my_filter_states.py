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
        db=sys.argv[3],
    )
    searchname = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (searchname,))
    for name in cursor.fetchall():
        print(name)
    cursor.close()
    db.close()
