#!/usr/bin/python3
"""
connect to database and query it
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def query_first_state(argument_list):
    """
    returns all records that match the given filter
    from states table from given database
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

    first_state = current_session.query(State).one_or_none(State.id == 1)

    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("")


if __name__ == "__main__":
    query_first_state(sys.argv)
