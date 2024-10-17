#!/etc/bin/python3

# before running this create the database people_things from within mysql
# run using: sudo python3 youtube-neuralnine-sqlalchemy.notes.py

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL


Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    
    ssn = Column("ssn", Integer, primary_key=True)
    first = Column("first_name", String(127))	
    last = Column("last_name", String(127))	
    gender = Column("gender", CHAR)	
    age = Column("age", Integer)	
    
    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.first = first
        self.last = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.first} {self.last} ({self.gender}, {self.age})"
    
class Thing(Base):
    __tablename__ = "things"
    
    identity = Column("id", Integer, primary_key=True)
    description = Column("description", String(127))
    owner = Column("owner", ForeignKey("people.ssn"))

    def __init__(self, identity, description, owner):
        self.identity = identity
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.identity}) {self.description} owned by {self.owner}"

# format : mysql://user:password@localhost:port/database_name
# from sqlalchemy docs : dialect+driver://username:password@host:port/database
# db_engine = create_engine("mysql://user:password@localhost:3306/database_name")

db_url = URL.create(
        "mysql",
        username="root",
        password="",
        host="localhost",
        database="people_things")

db_engine = create_engine(db_url, echo=True)
Base.metadata.create_all(bind=db_engine)
Session = sessionmaker(bind=db_engine)
current_session = Session()

p1 = Person(1, "Mike", "Smith", "m", 35)
p2 = Person(2, "Anna", "Blue", "f", 40)
p3 = Person(3, "Bob", "Blue", "m", 35)
p4 = Person(4, "Angela", "Colt", "f", 22)

t1 = Thing(1, "car", p1.ssn)
t2 = Thing(2, "laptop", p1.ssn)
t3 = Thing(3, "PS5", p2.ssn)
t4 = Thing(4, "electric drill", p3.ssn)
t5 = Thing(5, "book: crime and punishment", p3.ssn)

current_session.add(p1)
current_session.add(p2)
current_session.add(p3)
current_session.add(p4)

current_session.add(t1)
current_session.add(t2)
current_session.add(t3)
current_session.add(t4)
current_session.add(t5)

current_session.commit()

query1_results = (
        current_session.query(Thing, Person)
        .filter(Thing.owner == Person.ssn)
        .filter(Person.first == "Anna")
        )

for result in query1_results: 
    print(result)
