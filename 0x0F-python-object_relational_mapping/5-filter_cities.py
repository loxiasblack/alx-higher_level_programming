#!/usr/bin/python3
"""scripts that take states as argument and list all cities of the state"""

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
    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name  LIKE '{}'".format(sys.argv[4]))

    result = cursor.fetchall()
    city_names = ', '.join(city[0] for city in result)
    print(city_names)

    cursor.close()
    db.close()
