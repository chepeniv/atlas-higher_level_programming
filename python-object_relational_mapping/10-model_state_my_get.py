#!/usr/bin/python3
"""
connect to database and query it
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def query_state_name(argument_list):
    """
    returns all records that match the given filter
    from states table from given database
    """

    username = argument_list[1]
    password = argument_list[2]
    database = argument_list[3]
    statename = argument_list[4]

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database)

    db_engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(db_engine)
    current_session = Session()

    found_state = (
            current_session
            .query(State)
            .filter(State.name == statename)
            .one_or_none()
            )

    if found_state is not None:
        print("{}".format(found_state.id))
    else:
        print("Not found")


if __name__ == "__main__":
    query_state_name(sys.argv)
