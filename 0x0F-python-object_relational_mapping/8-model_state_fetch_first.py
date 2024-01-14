#!/usr/bin/python3
"""this fetches in the database"""


from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

username = argv[1]
password = argv[2]
database = argv[3]
host = "localhost"
connection = f'mysql+mysqldb://{username}:{password}@{host}:3306/{database}'

engine = create_engine(connection)

Session = sessionmaker(bind=engine)
session2 = Session()

state = session2.query(State).order_by(State.id.asc()).first()
if state:
    print(f"{state.id}: {state.name}")
else:
    print("Nothing")
