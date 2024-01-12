#!/usr/bin/python3
"""Scripts that lists all cities from databases"""

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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
