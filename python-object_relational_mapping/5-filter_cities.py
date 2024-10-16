#!/usr/bin/python3
""" module demonstrating the use of mysql with python """

import sys
import MySQLdb


def list_matching_states(params):
    """ function that accesses database and outputs entries """

    usa_db = MySQLdb.connect(
            user=params[1],
            passwd=params[2],
            database=params[3])

    db_cursor = usa_db.cursor()

    db_cursor.execute(
            "SELECT cities.name\
            FROM cities LEFT JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id", (params[4],))

    cities = db_cursor.fetchall()
    cities_count = len(cities)
    i = 0 
    while i < cities_count:
        city = cities[i][0]
        print("{}".format(city), end="")
        if i != cities_count - 1:
            print(", ", end="")
        else:
            print("")
        i += 1


if __name__ == "__main__":
    list_matching_states(sys.argv)
