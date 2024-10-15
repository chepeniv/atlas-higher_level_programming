#!/usr/bin/python3
""" module demonstrating the use of mysql with python """

import sys
import MySQLdb

def list_all_states(params):
    """ function that accesses database and outputs entries """
    usa_db = MySQLdb.connect(user=params[1], passwd=params[2], database=params[3])
    db_cursor = usa_db.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id")
    usa_states = db_cursor.fetchall()
    for state in usa_states:
        print("{}".format(state))

if __name__ == "__main__":
    params = sys.argv
    list_all_states(params)
