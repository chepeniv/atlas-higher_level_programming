#!/usr/bin/python3
"""
connect to database and query it
"""

from model_state import Base, State
from sqlalchemy import create_engine, sessionmaker
import sys


def query_all_states(argument_list):
    """
    returns all records from states table from given database
    """

    username = argument_list[1]
    password = argument_list[2]
    database = argument_list[3]

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database)

    db_engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(db_engine)
    current_session = Session()

    all_states = current_session.query(State)

    for state in all_states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    query_all_states(sys.argv)
