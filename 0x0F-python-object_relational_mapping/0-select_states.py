#!/usr/bin/python3
import MySQLdb
import sys


def list_states(username, passname, dbname):
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=passname,
                         db=dbname)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        passname = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, passname, dbname)
