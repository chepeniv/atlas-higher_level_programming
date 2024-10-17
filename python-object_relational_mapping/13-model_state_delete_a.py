#!/usr/bin/python3
"""
connect to database and add and remove matching records
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def delete_all_a(argument_list):
    """
    remove matching entries from states table
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

    found_state = (
            current_session.query(State)
            .filter(State.name.like('%a%'))
            .delete(synchronize_session=False)
            )

    current_session.commit()


if __name__ == "__main__":
    delete_all_a(sys.argv)
