#!/usr/bin/python3
""" module setting up a Base class and Derived class for mysql
""" 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

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
    '''
    def __str__(self):
        return f"{self.identity}: {self.name}"
    '''

if __name__ == "__main__":
    # db_engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_6_usa")

    db_engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(bind=db_engine)
