#!/usr/bin/python3
"""this fecthes things"""


from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """this is makes main"""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    host = "localhost"
    connection = f'mysql+mysqldb://{username}:\
        {password}@{host}:3306/{database}'

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session1 = Session()

    states = session1.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")
