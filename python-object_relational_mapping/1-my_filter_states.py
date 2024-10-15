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
    db_cursor.execute("SELECT * FROM states WHERE states.name = %s", (params[4],))

    for state in db_cursor.fetchall():
        print("{}".format(state))
    
    db_cursor.close()
    usa_db.close()


if __name__ == "__main__":
    list_matching_states(sys.argv)
