#!/usr/bin/python3
""" module demonstrating the use of mysql with python """

import sys
import MySQLdb


def list_N_states(params):
    """ function that accesses database and outputs entries """

    usa_db = MySQLdb.connect(
            user=params[1],
            passwd=params[2],
            database=params[3])

    db_cursor = usa_db.cursor()
    db_cursor.execute("SELECT * FROM states\
            WHERE LOWER(name) LIKE LOWER('n%')\
            ORDER BY id")

    for state in db_cursor.fetchall():
        print("{}".format(state))


if __name__ == "__main__":
    list_N_states(sys.argv)
