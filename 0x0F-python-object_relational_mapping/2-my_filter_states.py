#!/usr/bin/python3
"""script that diplay all states that maches the name argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    user=sys.argv[1]
    passwd=sys.argv[2]
    dbname=sys.argv[3]
    statename=sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=dbname
    )
    
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    cursor = db.cursor()
    cursor.execute(query, (statename,))
    for name in cursor.fetchall():
        print(name)
    cursor.close()
    db.close()
