#!/usr/bin/python3
"""
module setting up a Base class and Derived class for mysql
"""

from model_state import State
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


class City(Base):
    """
    definition of class that links to mysql table
    """
    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False)

    name = Column(
            String(128),
            nullable=False)

    state_id = Column(
            ForeignKey("states.id"),
            nullable=False)

    '''
    def __init__(self, identity, name):
        self.identity = identity
        self.name = name

    def __str__(self):
        return f"{self.identity}: {self.name}"
    '''


if __name__ == "__main__":
    db_engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(db_engine)
