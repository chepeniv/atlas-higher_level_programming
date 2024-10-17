#!/usr/bin/python3
"""
connect to database and add predefined entry to predefined table
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def insert_louisiana(argument_list):
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

    louisiana = State(name="Louisiana")

    current_session.add(louisiana)
    current_session.commit()

    print("{}".format(louisiana.id))


if __name__ == "__main__":
    insert_louisiana(sys.argv)
