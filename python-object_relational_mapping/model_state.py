#!/usr/bin/python3
""" module setting up a Base class and Derived class for mysql
""" 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """ definition of class that links to mysql table """ 
    __tablename__ = 'states'

    identity = Column(
            "id",
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False)

    name = Column(String(128), nullable=False)

    def __init__(self, identity, name):
        self.identity = identity
        self.name = name

    def __str__(self):
        return f"{self.identity}: {self.name}"
