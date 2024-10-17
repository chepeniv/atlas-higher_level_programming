#!/usr/bin/python3
"""
connect to database and add update entry
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def update_entry_id_2(argument_list):
    """
    update a single entry that matches predefined id
    in states table from given database
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
            .filter(State.id == 2)
            .update({'name': 'New Mexico'})
            )

    current_session.commit()


if __name__ == "__main__":
    update_entry_id_2(sys.argv)
