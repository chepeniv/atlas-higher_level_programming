```python
#!/usr/bin/python3
""" task rough guidelines
use SQLAlchemy
connect to a mysql server on localhost port 3306

classes inheriting from Base must be imported 
before calling `Base.metadata.create_all(engine)`

instance Base = declarative_base()
class def of State
    inherits from Base
    links to the mysql table `states`
    id : auto gen, unique int, cant be null, primary key
    name : max 128 char, cant be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

# basic usage
Base = declarative_base()
class derivedClass(Base):
    __tablename__ = 'some_table'
    identity = Column(Integer, primary_key=True)
    field_name = Column("alt_field_name", String(50))

# access mapped table
derivedClass.__table__

# access mapper
derivedClass.__mapper__

# adding a new attribute 
derivedClass.data = Column('new_field', Unicode)

# what the heck is RelatedInfo ?
derivedClass.related = relationship(RelatedInfo)

# classes that are constructed with declarative 
# interact freely with classes explicitly mapped with mapper()
# i don't know what this means

# it is recommended that all tables share the same underlying 
# MetaData object

# accessing metadata
db_engine = create_engine('sqlite://')
Base.metadata.create_all(db_engine)

# setting up with preexisting metadata 
other_metadata = MetaData()
Base = declarative_base(metadata=other_metadata)

"""
"""

def execute(params):
    """ function that accesses database and outputs entries """
    return None


if __name__ == "__main__":
    execute(sys.argv)
```
