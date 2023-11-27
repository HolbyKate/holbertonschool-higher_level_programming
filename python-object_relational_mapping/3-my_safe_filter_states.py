#!/usr/bin/python3
"""But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys


if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '%s' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()