#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, password=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    for state in cur.fetchall():
        print(state)
        
    cur.close()
    db.close()
