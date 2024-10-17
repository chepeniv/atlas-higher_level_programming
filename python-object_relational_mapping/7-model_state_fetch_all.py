#!/usr/bin/python3
""" module setting up a Base class and Derived class for mysql
""" 

from sqlalchemy.ext.declarative import declarative_base
from model_states import State, Base

def query(params)
    """ definition of class that links to mysql table """ 
    __tablename__ = 'states'
    identity = Column(
            "id",
            Integer(11),
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    query(sys.argv)
