#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
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
    query = "SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
